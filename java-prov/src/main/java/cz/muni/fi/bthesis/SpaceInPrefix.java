package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;


public class SpaceInPrefix extends TestCase {

    public SpaceInPrefix() {
        setFilename("space_in_prefix");
    }

    @Override
    public Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex ex", "https://example.org/");
        ns.register("ex", "https://example.com/");
        var e = ns.qualifiedName("ex ex", "e", factory);
        var a = ns.qualifiedName("ex", "a", factory);
        Entity entity = factory.newEntity(e);
        Activity activity = factory.newActivity(a);
        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(activity);
        document.setNamespace(ns);
        return document;
    }
}
