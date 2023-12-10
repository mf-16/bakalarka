using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace TestCases
{
    public class TestRunnerService
    {
        private Dictionary<string, Tuple<string, string>> config = new Dictionary<string, Tuple<string, string>> {
            { "python",new Tuple<string, string>("main.py",$"C:\\Users\\{Environment.UserName}\\bakalarka\\python-prov\\src")},
            { "java", new Tuple<string, string>("-jar target\\test-1.0-SNAPSHOT.jar",$"C:\\Users\\{Environment.UserName}\\bakalarka\\java-prov")}
        };
        public TestRunnerService() { }
        public void RunProcess(TestCaseResult result, string executable, string testScenario, string technique, string format)
        {
            Directory.SetCurrentDirectory(config[executable].Item2);
            Process process = new Process();
            process.StartInfo.FileName = executable;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.RedirectStandardError = true;
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.Arguments = $"{config[executable].Item1} {testScenario} {format} {technique}";

            process.Start();

            string output = process.StandardOutput.ReadToEnd();
            string errorOutput = process.StandardError.ReadToEnd();
            Console.WriteLine($"{executable} output:");
            Console.WriteLine(output + errorOutput);
            process.WaitForExit();
            if (process.ExitCode != 0)
            {
                if (technique == "s")
                {
                    result.Exception = errorOutput;
                }
                else
                {
                    if (output != "")
                    {
                        result.Result = true;
                    }
                    result.Exception = errorOutput;
                }
            }
            else
            {
                if (technique == "s")
                {
                    result.Result = true;
                    result.SerializedDocument = output;
                }
                else
                {
                    result.Result = true;
                    result.DeserializedDocument = output;
                }
            }
            process.Close();
        }
    }
}
