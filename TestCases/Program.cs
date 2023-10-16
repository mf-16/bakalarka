


using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {

        string? input = "";
        while (input != "q")
        {
            try
            {
                Console.Write($">>> ");
                input = Console.ReadLine();
                var args = input.Trim().Split(" ");
                var testCase = args[0];
                var format = args[1];
                var serialize = args[2];
                var deserialize = args[3];
                if (serialize == "p" && deserialize == "j")
                {
                    RunPython(testCase, "s", format);
                    RunJava(testCase, "d", format);
                }
                else if (serialize == "j" && deserialize == "p")
                {
                    RunJava(testCase, "s", format);
                    RunPython(testCase, "d", format);
                }
                else
                {
                    throw new Exception();
                }


            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        Console.WriteLine("QUIT");
    }
    public static void RunPython(string testScenario, string technique, string format)
    {
        Directory.SetCurrentDirectory($"C:\\Users\\{Environment.UserName}\\bakalarka\\python-prov\\src");
        Process pythonProcess = new Process();
        pythonProcess.StartInfo.FileName = "python";
        pythonProcess.StartInfo.RedirectStandardOutput = true;
        pythonProcess.StartInfo.RedirectStandardError = true;
        pythonProcess.StartInfo.UseShellExecute = false;
        pythonProcess.StartInfo.CreateNoWindow = true;
        pythonProcess.StartInfo.Arguments = $"main.py {testScenario} {format} {technique}";

        pythonProcess.Start();

        string output = pythonProcess.StandardOutput.ReadToEnd();
        string errorOutput = pythonProcess.StandardError.ReadToEnd();
        Console.WriteLine("Python Output:");
        Console.WriteLine(output + errorOutput);
        pythonProcess.WaitForExit();
        pythonProcess.Close();
        Console.ReadKey();
    }
    public static void RunJava(string testScenario, string technique, string format)
    {
        Directory.SetCurrentDirectory($"C:\\Users\\{Environment.UserName}\\bakalarka\\java-prov");
        Process javaProcess = new Process();
        javaProcess.StartInfo.FileName = "java";
        javaProcess.StartInfo.Arguments = $"-jar target\\test-1.0-SNAPSHOT-shaded.jar {testScenario} {format} {technique}";
        javaProcess.StartInfo.RedirectStandardOutput = true;
        javaProcess.StartInfo.RedirectStandardError= true;
        javaProcess.StartInfo.UseShellExecute = false;
        javaProcess.StartInfo.CreateNoWindow = true;

        javaProcess.Start();

        string output = javaProcess.StandardOutput.ReadToEnd();
        string errorOutput = javaProcess.StandardError.ReadToEnd();
        Console.WriteLine("Java Output:");
        Console.WriteLine(output + errorOutput);
        javaProcess.WaitForExit();
        javaProcess.Close();
        Console.ReadKey();
    }
}

