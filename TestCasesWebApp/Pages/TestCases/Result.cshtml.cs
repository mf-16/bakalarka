using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using TestCases;

namespace TestCasesWebApp.Pages.TestCases
{
    public class ResultModel : PageModel
    {
        private TestRunnerService TestRunnerService { get; set; }

        private CommandProcessor CommandProcessor { get; set; }
        [BindProperty]
        public TestCaseResult TestCaseResult { get; set; }

        public ResultModel() {
            TestRunnerService = new TestRunnerService();
            CommandProcessor = new CommandProcessor(TestRunnerService);
        }
        public void OnGet()
        {
            string command = TempData["Command"] as string;
            TestCaseResult = CommandProcessor.ProcessCommand(command);
            TestCaseResult.Exception = "Not Implemented Exception";
            TestCaseResult.Description = "PROVN deserialization is not implemented yet";



        }
        public IActionResult OnPost()
        {

            TempData["Exception"] = TestCaseResult.Exception;
            TempData["Description"] = TestCaseResult.Description;
            return RedirectToPage("/TestCases/Ahoj");
        }
    }
}
