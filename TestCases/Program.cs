


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
            catch (FormatException)
            {
                Console.WriteLine("Invalid argument. Use -h.");
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
        Directory.SetCurrentDirectory("C:\\Users\\Matúš\\bakalarka\\python-prov\\src");
        // Create a new process to run Python
        Process pythonProcess = new Process();
        pythonProcess.StartInfo.FileName = "python"; // or specify the path to your Python interpreter
        pythonProcess.StartInfo.RedirectStandardOutput = true;
        pythonProcess.StartInfo.UseShellExecute = false;
        pythonProcess.StartInfo.CreateNoWindow = true;

        // Specify the Python script or command you want to run
        pythonProcess.StartInfo.Arguments = $"main.py {testScenario} {format} {technique}";

        // Start the Python process
        pythonProcess.Start();

        // Read the output (if needed)
        string output = pythonProcess.StandardOutput.ReadToEnd();
        Console.WriteLine("Python Output:");
        Console.WriteLine(output);

        // Wait for the Python process to exit
        pythonProcess.WaitForExit();

        // Close the Python process
        pythonProcess.Close();

        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }
    public static void RunJava(string testScenario, string technique, string format)
    {
        Directory.SetCurrentDirectory("C:\\Users\\Matúš\\bakalarka\\java-prov");
        // Create a new process to run the Java JAR file
        Process javaProcess = new Process();
        javaProcess.StartInfo.FileName = "java"; // or specify the full path to the java executable
        javaProcess.StartInfo.Arguments = $"-jar test-1.0-SNAPSHOT-shaded.jar {testScenario} {format} {technique}"; // specify the JAR file
        javaProcess.StartInfo.RedirectStandardOutput = true;
        javaProcess.StartInfo.UseShellExecute = false;
        javaProcess.StartInfo.CreateNoWindow = true;

        // Start the Java process
        javaProcess.Start();

        // Read the output (if needed)
        string output = javaProcess.StandardOutput.ReadToEnd();
        Console.WriteLine("Java Output:");
        Console.WriteLine(output);

        // Wait for the Java process to exit
        javaProcess.WaitForExit();

        // Close the Java process
        javaProcess.Close();

        Console.WriteLine("Press any key to exit.");
        Console.ReadKey();
    }
    public void ParseArguments()
    {
        
    }
}

