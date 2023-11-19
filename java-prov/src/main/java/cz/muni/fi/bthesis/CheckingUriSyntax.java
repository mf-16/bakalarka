package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;


public class CheckingUriSyntax extends TestCase {

    public CheckingUriSyntax() {
        setFilename("checking_uri_syntax");
    }

    public Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex", "http://www.w3. org/ns/prov#");
        var e = ns.qualifiedName("ex", "e", factory);
        Entity entity = factory.newEntity(e);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        return document;
    }
}
