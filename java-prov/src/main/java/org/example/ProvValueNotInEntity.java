package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Attribute;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.util.ArrayList;


public class ProvValueNotInEntity implements TestCase {

    public void serialize(String format) {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org");
        var a = ns.qualifiedName("ex","ac",factory);
        var attributes = new ArrayList<Attribute>();
        Attribute at = factory.newValue(1);
        attributes.add(at);
        Activity activity = factory.newActivity(a,null,null,attributes);
        document.getStatementOrBundle().add(activity);
        document.setNamespace(ns);

        writeDocument(format,document,"prov_value_not_in_entity");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/prov_value_not_in_entity.%s", format));
        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }

    @Override
    public Document createDocument() {
        return null;
    }
}
