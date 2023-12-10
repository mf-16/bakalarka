using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using TestCases;

namespace TestCasesWebApp.Pages.TestCases
{
    public class IndexModel : PageModel
    {

        public SelectList testCaseComboBox = new SelectList(new List<SelectListItem>
        {
            new SelectListItem { Value = "default_namespace", Text = "Default namespace" },
            new SelectListItem { Value = "escaped_characters", Text = "Escaped characters" },
            new SelectListItem { Value = "checking_uri_syntax", Text = "Checking uri syntax" },
        }, "Value", "Text");
        public SelectList formatComboBox = new SelectList(new List<SelectListItem>
        {
            new SelectListItem { Value = "provn", Text = "PROVN" },
            new SelectListItem { Value = "json", Text = "JSON" },
            new SelectListItem { Value = "xml", Text = "XML" },
        }, "Value", "Text");
        public SelectList executableCombobox = new SelectList(new List<SelectListItem>
        {
            new SelectListItem { Value = "python java", Text = "python-java" },
            new SelectListItem { Value = "java python", Text = "java-python" },
        }, "Value", "Text");
        [BindProperty]
        public string? TestCase {  get; set; }
        [BindProperty]
        public string? Format { get; set; }
        [BindProperty]
        public string? Executable {  get; set; }

        public IndexModel()
        {
        }

        public void OnGet()
        {
        }
        public IActionResult OnPost()
        {
            string command = TestCase + " " + Format + " " + Executable;
       
            TempData["Command"] = command;
            return RedirectToPage("/TestCases/Result");
        }
    }
}
