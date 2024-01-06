using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace TestCases
{
    public class TestRunnerService
    {
        private Dictionary<string, Tuple<string, string>> config = new Dictionary<string, Tuple<string, string>> {
            { "python",new Tuple<string, string>("main.py",Path.Combine("python-prov", "src"))},
            { "java", new Tuple<string, string>("-jar target\\test-1.0-SNAPSHOT.jar", "java-prov")}
        };
        public TestRunnerService() { }
        private void ConfigureProcess(Process process, string executable, string testScenario, string technique, string format)
        {
            process.StartInfo.FileName = executable;
            process.StartInfo.WorkingDirectory = Path.Combine(GetRootDirectory(AppDomain.CurrentDomain.BaseDirectory), config[executable].Item2);
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.RedirectStandardError = true;
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.Arguments = $"{config[executable].Item1} {testScenario} {format} {technique}";
        }
        private void AttachOutputHandlers(Process process, StringBuilder outputBuilder, StringBuilder errorBuilder)
        {
            process.OutputDataReceived += (sender, e) => outputBuilder.AppendLine(e.Data);
            process.ErrorDataReceived += (sender, e) => errorBuilder.AppendLine(e.Data);
        }
        private void LogProcessOutput(string executable, string output)
        {
            Console.WriteLine($"{executable} output:");
            Console.WriteLine(output);
        }
        private void ProcessExitHandling(Process process, TestCaseResult result, string technique, string output, string errorOutput)
        {
            if (process.ExitCode != 0)
            {
                HandleExitCodeNotZero(result, technique, output, errorOutput);
            }
            else
            {
                HandleExitCodeZero(result, technique, output);
            }
        }

        private void HandleExitCodeNotZero(TestCaseResult result, string technique, string output, string errorOutput)
        {
            if (technique == "s")
            {
                result.Exception = errorOutput.Trim();
            }
            else
            {
                result.Result = output.Split(new string[] { Environment.NewLine }, StringSplitOptions.None)[0].ToLower() == "true";
                if (result.Exception == null)
                {
                    result.Exception = errorOutput.Trim();
                }
            }
        }

        private void HandleExitCodeZero(TestCaseResult result, string technique, string output)
        {
            if (technique == "s")
            {
                result.SerializedDocument = output.Trim();
            }
            else
            {
                string delimiter = "----------";
                result.Result = output.Split(new string[] { Environment.NewLine }, StringSplitOptions.None)[0].ToLower() == "true";
                result.DeserializedDocument = output.Substring(output.IndexOf(delimiter) + delimiter.Length).Trim();
            }
        }
        public static string GetRootDirectory(string startingDirectory)
        {
            string resultDirectory = Path.Combine(startingDirectory, "..", "..", "..", "..", "..");

            resultDirectory = Path.GetFullPath(resultDirectory);

            return resultDirectory;
        }
        public void RunProcess(TestCaseResult result, string executable, string testScenario, string technique, string format)
        {
            using (Process process = new Process())
            {
                ConfigureProcess(process, executable, testScenario, technique, format);
                
                StringBuilder outputBuilder = new StringBuilder();
                StringBuilder errorBuilder = new StringBuilder();

                AttachOutputHandlers(process, outputBuilder, errorBuilder);

                process.Start();
                process.BeginOutputReadLine();
                process.BeginErrorReadLine();
                process.WaitForExit();

                LogProcessOutput(executable, outputBuilder.ToString() + errorBuilder.ToString());
                ProcessExitHandling(process, result, technique, outputBuilder.ToString(), errorBuilder.ToString());


            }
        }
    }
}
