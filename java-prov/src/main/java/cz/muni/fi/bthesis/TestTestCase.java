package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.*;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.util.LinkedList;
import java.util.List;

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
        var des = new QualifiedNameUtils();
        var localName = "='(),-:;[].";
        System.out.println(des.escapeProvLocalName(localName));
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex", "https://example.org/");
        var e = ns.qualifiedName("ex","a",factory);
        var a = ns.qualifiedName("ex","e",factory);
        Entity entity = factory.newEntity(e);
        Activity activity = factory.newActivity(a);
        WasGeneratedBy wasGeneratedBy = factory.newWasGeneratedBy(null,e,a);
        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(activity);
        document.getStatementOrBundle().add(wasGeneratedBy);

        document.setNamespace(ns);
        return document;
    }
}
