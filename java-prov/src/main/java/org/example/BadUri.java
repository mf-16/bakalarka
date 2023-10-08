package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.ProvFactory;
import org.openprovenance.prov.vanilla.Document;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;


public class BadUri implements TestCase {
    public void serialize(String format){
        var inf = new InteropFramework();
        ProvFactory factory = InteropFramework.getDefaultFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","http://www.w3. org/ns/prov#");
        document.setNamespace(ns);

        var formatType = inf.getTypeForFormat(format);

        File file = new File(String.format("../python-prov/data/bad_uri.%s", format));
        try {
            OutputStream outputStream = new FileOutputStream(file);
            inf.writeDocument(outputStream, formatType, document);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public void deserialize(String format) {
       var inf = new InteropFramework();
       var document = inf.readDocumentFromFile(String.format("data/bad_uri.%s",format));
       inf.writeDocument("data/temp.provn",document);

    }
}
