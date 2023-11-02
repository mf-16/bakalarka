package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;


public class DefaultNamespace extends TestCase {

    public DefaultNamespace(){
        setFilename("default_namespace");
    }

    @Override
    public Document createDocument() {
        ProvFactory factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.registerDefault("https://default.org/");
        ns.register("ex","https://example.org/");
        var e = ns.qualifiedName("ex","e",factory);
        Entity entity = factory.newEntity(e);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        return document;
    }
}
