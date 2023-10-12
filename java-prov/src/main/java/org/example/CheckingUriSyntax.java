package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.ProvFactory;
import org.openprovenance.prov.vanilla.Document;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;


public class CheckingUriSyntax implements TestCase {
    public void serialize(String format){
        var inf = new InteropFramework();
        ProvFactory factory = new org.openprovenance.prov.vanilla.ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","http://www.w3. org/ns/prov#");
        document.setNamespace(ns);

        writeDocument(format,document,"checking_uri_syntax");
    }
    public void deserialize(String format) {
       var inf = new InteropFramework();
       var document = inf.readDocumentFromFile(String.format("data/checking_uri_syntax.%s",format));
       var formatType = inf.getTypeForFormat(format);
       inf.writeDocument(System.out, formatType, document);
    }
}
