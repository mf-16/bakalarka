package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.ProvFactory;


public class BadUri {
    public static void perform() {
       var inf = new InteropFramework();
//        ProvFactory factory = InteropFramework.newXMLProvFactory();
//        var document = new Document();
//        var ns = new Namespace();
//        ns.addKnownNamespaces();
//        ns.register("ex","http://www.w3. org/ns/prov#");
//        document.setNamespace(ns);
       var document = inf.readDocumentFromFile("bad_uri.provn");
       inf.writeDocument("temp.provn",document);

    }
}
