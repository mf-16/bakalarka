using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Newtonsoft.Json;
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
            new SelectListItem { Value = "local_part_of_id_with_space", Text = "Local part of id with space" },
            new SelectListItem { Value = "loss_of_microseconds", Text = "Loss of microseconds" },
            new SelectListItem { Value = "loss_of_timezone", Text = "Loss of timezone" },
            new SelectListItem { Value = "multiple_prov_value", Text = "Multiple prov value" },
            new SelectListItem { Value = "nonsense_prov_records", Text = "Nonsense prov records" },
            new SelectListItem { Value = "prov_record_without_id", Text = "Prov record without id" },
            new SelectListItem { Value = "prov_value_not_in_entity", Text = "Prov value not in entity" },
            new SelectListItem { Value = "space_in_prefix", Text = "Space in prefix" },
            new SelectListItem { Value = "top_instance_namespace_bundle", Text = "Top instance namespace bundle" },
            new SelectListItem { Value = "implicit_existence_of_prov_namespace", Text = "Implicit existence of prov namespace" }

        }, "Value", "Text");
        public SelectList formatComboBox = new SelectList(new List<SelectListItem>
        {
            new SelectListItem { Value = "provn", Text = "PROVN" },
            new SelectListItem { Value = "json", Text = "JSON" },
            new SelectListItem { Value = "xml", Text = "XML" },
        }, "Value", "Text");
        public SelectList executableCombobox = new SelectList(new List<SelectListItem>
        {
            new SelectListItem { Value = "java", Text = "java" },
            new SelectListItem { Value = "python", Text = "python" }
        }, "Value", "Text");
        [BindProperty]
        public string? TestCase {  get; set; }
        [BindProperty]
        public string? Format { get; set; }
        [BindProperty]
        public string? SerializeIn {  get; set; }
        [BindProperty]
        public string? DeserializeIn { get; set; }

        private TestRunnerService TestRunnerService { get; set; }

        private CommandProcessor CommandProcessor { get; set; }

        public IndexModel()
        {
            TestRunnerService = new TestRunnerService();
            CommandProcessor = new CommandProcessor(TestRunnerService);
        }

        public void OnGet()
        {
            SerializeIn = "java";
            DeserializeIn = "python";

        }
        public IActionResult OnPost()
        {
            string command = TestCase + " " + Format + " " + SerializeIn + " " + DeserializeIn;
            TestCaseResult testCaseResult = CommandProcessor.ProcessCommand(command);

            string descFile = TestCase + "_" + Format + "_" + SerializeIn + "_" + DeserializeIn + "_desc.txt";
            string descFilePath = Path.Combine("AppData", "Descriptions", descFile);
            testCaseResult.Description = System.IO.File.ReadAllText(descFilePath);

            string testCaseResultJson = JsonConvert.SerializeObject(testCaseResult);
            string filePath = Path.Combine("AppData", "testCaseResult.json");
            System.IO.File.WriteAllText(filePath, testCaseResultJson);
            
            return RedirectToPage("/TestCases/Result");
        }
    }
}
