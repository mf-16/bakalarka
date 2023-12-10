using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace TestCasesWebApp.Pages.TestCases
{
    public class AhojModel : PageModel
    {
        public string? Exception { get; set; }
        public string? Description { get; set; }
        public void OnGet()
        {
            Exception = TempData["Exception"] as string;
            Description = TempData["Description"] as string;
        }
    }
}
