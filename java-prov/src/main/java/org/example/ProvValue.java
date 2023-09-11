package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Document;


public class ProvValue {
    public static void perform() {
        var inf = new InteropFramework();
        Document document = inf.readDocumentFromFile("prov_value.provn");
        inf.writeDocument("temp.provn",document);

    }
}
