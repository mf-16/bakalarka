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

        public Dictionary<string, string> testCaseDescriptions = new Dictionary<string, string>()
        {
            { "default_namespace","This test evaluates library`s capability to safely use and preserve default namespace." },
            { "escaped_characters","This test examines capability of library to escape characters that should be escaped"},
            { "checking_uri_syntax","This test checks if library is validating the IRI when creating namespaces. The objective is to ensure that the library correctly identifies IRIs which are not correct."},
            {"local_part_of_id_with_space", "This test verifies whether the libraries correctly identifiu and reject identifier with space in its local part. For example: \"ex: a b c\" " },
            {"loss_of_microseconds","This test evaluates if the library is capable of not losing the microseconds when working with time instants." },
            {"loss_of_timezone","This test evaluates the ability of library to preserve timezones."},
            {"multiple_prov_value","This test evaluates the capability of library to correctly identify and reject entity records that contain multiple prov:value attributes, which is not allowed according to PROV-DM"},
            {"prov_record_without_id","This test evaluates ability to correctly handle relations without identifier."},
            {"prov_value_not_in_entity","The test evaluates the capability of library to identify and reject prov:value attributes not in entity, which is not allowed according to PROV-DM"},
            {"space_in_prefix","This test checks if library is validation the prefix during namespace declaration" },
        };

        public IndexModel()
        {
            TestRunnerService = new TestRunnerService();
            CommandProcessor = new CommandProcessor(TestRunnerService);
        }

        public void OnGet()
        {

        }
        public IActionResult OnPost()
        {
            string command = TestCase + " " + Format + " " + SerializeIn + " " + DeserializeIn;
            TestCaseResult testCaseResult = CommandProcessor.ProcessCommand(command);

            string descFile = TestCase + "_" + Format + "_" + SerializeIn + "_" + DeserializeIn + "_desc.txt";
            string descFilePath = Path.Combine("AppData", "Descriptions", descFile);
            testCaseResult.Description = System.IO.File.ReadAllText(descFilePath);

            string startDocument = TestCase + ".provn";
            string startDocumentPath = Path.Combine("AppData", "ProvnFiles", startDocument);
            testCaseResult.StartDocument = System.IO.File.ReadAllText(startDocumentPath);

            string testCaseResultJson = JsonConvert.SerializeObject(testCaseResult);
            string filePath = Path.Combine("AppData", "testCaseResult.json");
            System.IO.File.WriteAllText(filePath, testCaseResultJson);
            
            return RedirectToPage("/TestCases/Result");
        }
        public IActionResult OnGetDescription(string selectedTestCase)
        {
            if (testCaseDescriptions.ContainsKey(selectedTestCase))
            {
                return new JsonResult(testCaseDescriptions[selectedTestCase]);
            }
            else
            {
                return new NotFoundResult();
            }
        }
    }
}
