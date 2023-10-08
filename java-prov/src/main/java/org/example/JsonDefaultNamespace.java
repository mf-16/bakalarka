package org.example;

import org.openprovenance.prov.interop.Formats;
import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;


public class JsonDefaultNamespace implements TestCase {

    public void serialize(String format) {
        ProvFactory factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.registerDefault("default");
        ns.register("ex","https://example.org");
        var eqn = ns.qualifiedName("ex","entity",factory);
        Entity entity = factory.newEntity(eqn);
        var qn = ns.qualifiedName("xsd","string",factory);
        entity.setValue(factory.newValue(1,qn));
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);


        var inf = new InteropFramework();
        var formatType = inf.getTypeForFormat(format);

        File file = new File(String.format("../python-prov/data/json_default_namespace.%s", format));
        try {
            OutputStream outputStream = new FileOutputStream(file);
            inf.writeDocument(outputStream, formatType, document);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/json_default_namespace.%s", format));
    }
}
