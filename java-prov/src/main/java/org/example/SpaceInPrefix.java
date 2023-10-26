package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;


public class SpaceInPrefix implements TestCase {
    public void serialize(String format) {
        var document = createDocument();

        writeDocument(format,document,"space_in_prefix");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/space_in_prefix.%s", format));

        var expectedDocument = createDocument();
        System.out.println(document.equals(expectedDocument));

        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }

    @Override
    public Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex ex","https://example.org/");
        ns.register("ex","https://example.com/");
        var e = ns.qualifiedName("ex ex","e",factory);
        var a = ns.qualifiedName("ex","a",factory);
        Entity entity = factory.newEntity(e);
        Activity activity = factory.newActivity(a);
        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(activity);
        document.setNamespace(ns);
        return document;
    }
}
