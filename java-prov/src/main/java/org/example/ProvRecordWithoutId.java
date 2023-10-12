package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.WasGeneratedBy;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;


public class ProvRecordWithoutId implements TestCase {

    public void serialize(String format) {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org");
        var e = ns.qualifiedName("ex","e",factory);
        var a = ns.qualifiedName("ex","a",factory);
        Entity entity = factory.newEntity(e);
        Activity activity = factory.newActivity(a);
        WasGeneratedBy wasGeneratedBy = factory.newWasGeneratedBy(null,e,a);
        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(activity);
        document.getStatementOrBundle().add(wasGeneratedBy);
        document.setNamespace(ns);

        writeDocument(format,document,"prov_record_without_id");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/prov_record_without_id.%s", format));
        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }
}
