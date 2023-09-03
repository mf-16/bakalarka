package org.example;

import org.openprovenance.prov.interop.InteropFramework;


public class BadUri {
    public static void perform() {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile("bad_uri.provn");
        inf.writeDocument("temp.provn",document);

    }
}
