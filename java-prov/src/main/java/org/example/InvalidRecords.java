package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Document;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.ProvFactory;


public class InvalidRecords implements TestCase {

    public void serialize(String format) {
        //TODO
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        Document document = inf.readDocumentFromFile(String.format("data/invalid_records.%s", format));
    }
}
