using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestCases
{
    public class TestRunnerService
    {
        private Dictionary<string, Tuple<string, string>> config = new Dictionary<string, Tuple<string, string>> {
            { "python",new Tuple<string, string>("main.py",$"C:\\Users\\{Environment.UserName}\\bakalarka\\python-prov\\src")},
            { "java", new Tuple<string, string>("-jar target\\test-1.0-SNAPSHOT.jar",$"C:\\Users\\{Environment.UserName}\\bakalarka\\java-prov")}
        };
        public TestRunnerService() { }
        public void RunProcess(string executable, string testScenario, string technique, string format)
        {
            
            Directory.SetCurrentDirectory(config[executable].Item2);
            Process pythonProcess = new Process();
            pythonProcess.StartInfo.FileName = executable;
            pythonProcess.StartInfo.RedirectStandardOutput = true;
            pythonProcess.StartInfo.RedirectStandardError = true;
            pythonProcess.StartInfo.UseShellExecute = false;
            pythonProcess.StartInfo.CreateNoWindow = true;
            pythonProcess.StartInfo.Arguments = $"{config[executable].Item1} {testScenario} {format} {technique}";

            pythonProcess.Start();

            string output = pythonProcess.StandardOutput.ReadToEnd();
            string errorOutput = pythonProcess.StandardError.ReadToEnd();
            Console.WriteLine($"{executable} output:");
            Console.WriteLine(output + errorOutput);
            pythonProcess.WaitForExit();
            pythonProcess.Close();
            Console.ReadKey();
        }
    }
}
