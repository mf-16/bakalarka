package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;


public class LocalPartOfIdWithSpace implements  TestCase {

    public void serialize(String format) {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org");
        var eqn = ns.qualifiedName("ex","a b c",factory);
        Entity entity = factory.newEntity(eqn);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);

        writeDocument(format,document,"local_part_of_id_with_space");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/local_part_of_id_with_space.%s", format));
        var formatType = inf.getTypeForFormat(format);
        var factory = new ProvFactory();
        var document2 = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org/");
        var eqn = ns.qualifiedName("ex","a b c",factory);
        Entity entity = factory.newEntity(eqn);
        document2.getStatementOrBundle().add(entity);
        document2.setNamespace(ns);
        System.out.println(document.equals(document2));
        inf.writeDocument(System.out, formatType, document);
    }
}
