package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Attribute;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.Value;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.util.ArrayList;


public class MultipleProvValue extends TestCase {

    public MultipleProvValue(){
        setFilename("multiple_prov_value");
    }

    @Override
    public Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org/");
        var e = ns.qualifiedName("ex","e",factory);
        var attributes = new ArrayList<Attribute>();
        Attribute at = factory.newValue(1);
        Attribute at2 = factory.newValue(2);
        Attribute at3 = factory.newAttribute(ns.qualifiedName("prov","value",factory),3,ns.qualifiedName("xsd","int",factory));
        attributes.add(at);
        attributes.add(at2);
        attributes.add(at3);
        Entity entity = factory.newEntity(e,attributes);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        return document;
    }
}
