package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Document;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.ProvFactory;


public class InvalidRecords {
    public static void perform() {
        var inf = new InteropFramework();
        Document document = inf.readDocumentFromFile("invalid_records.provn");
        inf.writeDocument("temp.provn",document);

    }
}
