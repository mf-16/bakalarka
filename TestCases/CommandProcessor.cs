using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestCases
{
    public class CommandProcessor
    {   
        private TestRunnerService testRunner;
        private HashSet<string> executables = new HashSet<string> { "python", "java" };
        public CommandProcessor(TestRunnerService testRunner) {
            this.testRunner = testRunner;
        }
        public TestCaseResult ProcessCommand(string input)
        {
            var args = input.Trim().Split(" ");
            TestCaseResult testCaseResult;
            var testCase = args[0];
            var format = args[1];
            var serialize = args[2];
            var deserialize = args[3];
            string serOut = "";
            string desOut = "";
            if (executables.Contains(serialize) && executables.Contains(deserialize))
            {
                testCaseResult = new TestCaseResult(testCase);
                testRunner.RunProcess(testCaseResult, serialize, testCase, "s", format);
                testRunner.RunProcess(testCaseResult, deserialize, testCase, "d", format);
            }
            else
            {
                throw new Exception("invalid executable");
            }

            return testCaseResult;

        }

    }
}
