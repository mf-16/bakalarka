package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.HadMember;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

/**
 * @author Matus Formanek
 */
public class TestTestCase extends TestCase {
    public TestTestCase() {
        setFilename("test_test_case");
    }

    @Override
    public Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex", "https://example.org/");
        var e = ns.qualifiedName("ex", "e", factory);
        var col_id = ns.qualifiedName("ex", "c", factory);
        var col_prefix = ns.qualifiedName("prov", "Collection", factory);
        var provqn = ns.qualifiedName("prov", "QUALIFIED_NAME", factory);
        Entity collection = factory.newEntity(col_id);
        Entity entity = factory.newEntity(e);
        collection.getType().add(factory.newType(col_prefix, provqn));
        HadMember hadMember = factory.newHadMember(col_id, e);
        document.getStatementOrBundle().add(collection);
        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(hadMember);
        document.setNamespace(ns);
        return document;
    }
}
