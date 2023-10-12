package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;


public class DefaultNamespace implements TestCase {

    public void serialize(String format) {
        ProvFactory factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.registerDefault("https://default.org/");
        ns.register("ex","https://example.org");
        var eqn = ns.qualifiedName("ex","entity",factory);
        Entity entity = factory.newEntity(eqn);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);


        writeDocument(format,document,"default_namespace");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/default_namespace.%s", format));

        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }
}
