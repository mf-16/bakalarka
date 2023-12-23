using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Newtonsoft.Json;
using TestCases;

namespace TestCasesWebApp.Pages.TestCases
{
    public class ResultModel : PageModel
    {
        [BindProperty]
        public TestCaseResult TestCaseResult { get; set; }

        public ResultModel() {
        }
        public void OnGet()
        {
            string filePath = Path.Combine("AppData", "testCaseResult.json");

            if (System.IO.File.Exists(filePath))
            {
                string testCaseResultJson = System.IO.File.ReadAllText(filePath);
                TestCaseResult = JsonConvert.DeserializeObject<TestCaseResult>(testCaseResultJson);
            }
        }
    }
}
