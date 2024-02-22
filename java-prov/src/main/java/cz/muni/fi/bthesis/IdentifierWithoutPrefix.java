package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

/**
 * @author Matus Formanek
 */
public class IdentifierWithoutPrefix extends TestCase{
    public IdentifierWithoutPrefix(){
        setFilename("identifier_without_prefix");
    }
    @Override
    public Document createDocument() {
        ProvFactory factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.registerDefault("https://default.org/");
        var e = ns.qualifiedName(null, "e", factory);
        Entity entity = factory.newEntity(e);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        return document;
    }
}
