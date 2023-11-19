package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;


public class DefaultNamespace extends TestCase {

    public DefaultNamespace() {
        setFilename("default_namespace");
    }

    @Override
    public Document createDocument() {
        ProvFactory factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.registerDefault("https://default.org/");
        ns.register("ex", "https://example.org/");
        var e = ns.qualifiedName("ex", "e", factory);
        Entity entity = factory.newEntity(e);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        return document;
    }
}
