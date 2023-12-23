


using System;
using System.Diagnostics;
using TestCases;

class Program
{
    static void Main()
    {
        TestRunnerService testRunner = new TestRunnerService();
        CommandProcessor parser = new CommandProcessor(testRunner);
        string? input = "";
        while (input != "q")
        {
            try
            {   
                Console.Write($">>> ");
                input = Console.ReadLine();
                parser.ProcessCommand(input);


            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        Console.WriteLine("QUIT");
    }
}

