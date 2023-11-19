package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;


public class LocalPartOfIdWithSpace extends TestCase {

    public LocalPartOfIdWithSpace() {
        setFilename("local_part_of_id_with_space");
    }

    @Override
    public Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex", "https://example.org/");
        var eqn = ns.qualifiedName("ex", "a b c", factory);
        Entity entity = factory.newEntity(eqn);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        return document;
    }
}
