package org.example;

import org.openprovenance.prov.model.Attribute;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;
import org.openprovenance.prov.vanilla.QualifiedName;

import java.util.ArrayList;

/**
 * @author Matus Formanek
 */
public class ImplicitExistenceOfProvNamespace extends TestCase{

    public ImplicitExistenceOfProvNamespace(){
        setFilename("implicit_existence_of_prov_namespace");
    }
    @Override
    Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org/");
        var e = ns.qualifiedName("ex","e",factory);
        var value = factory.newType(1, factory.getName().XSD_INT);
        Entity entity = factory.newEntity(e);
        entity.getType().add(value);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        return document;
    }
}
