package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;


public class TopInstanceNamespaceBundle implements TestCase {

    public void serialize(String format) {
        ProvFactory factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.registerDefault("https://example.com");
        ns.register("ex","https://example.org");
        var ns2 = new Namespace();
        ns2.addKnownNamespaces();
        var e = ns.qualifiedName("ex","e",factory);
        var e2 = ns2.qualifiedName(null,"e2",factory);
        var a = ns.qualifiedName("ex","a",factory);
        Entity entity = factory.newEntity(e);
        Entity entity2 = factory.newEntity(e2);
        Activity activity = factory.newActivity(a);
        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(activity);
        document.setNamespace(ns);
        // BUNDLE
        var b = ns.qualifiedName(null,"b",factory);
        var bundle = factory.newNamedBundle(b,new ArrayList<>());
        bundle.getStatement().add(entity2);
        bundle.setNamespace(ns2);
        document.getStatementOrBundle().add(bundle);



        writeDocument(format,document,"top_instance_namespace_bundle");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/top_instance_namespace_bundle.%s", format));
        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }

    @Override
    public Document createDocument() {
        return null;
    }
}
