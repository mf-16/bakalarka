using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestCases
{
    [Serializable]
    public class TestCaseResult
    {
        public string Name { get; set; }
        public bool Result { get; set; }
        public string? SerializedDocument { get; set; }
        public string? DeserializedDocument { get; set; }

        public string? StartDocument { get; set; }
        public string? Exception { get; set; }
        public string?  Description { get; set; }
        public TestCaseResult()
        {

        }
        public TestCaseResult(string name)
        {
            Name = name;
        }

    }
}
