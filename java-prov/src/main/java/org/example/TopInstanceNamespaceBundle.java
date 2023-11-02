package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;


public class TopInstanceNamespaceBundle extends TestCase {

    public TopInstanceNamespaceBundle(){
        setFilename("top_instance_namespace_bundle");
    }

    @Override
    public Document createDocument() {
        ProvFactory factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org/");
        var ns2 = new Namespace();
        ns2.addKnownNamespaces();
        var e = ns.qualifiedName("ex","e",factory);
        var e2 = ns2.qualifiedName("ex","e2",factory);
        var a = ns.qualifiedName("ex","a",factory);
        Entity entity = factory.newEntity(e);
        Entity entity2 = factory.newEntity(e2);
        Activity activity = factory.newActivity(a);
        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(activity);
        document.setNamespace(ns);
        // BUNDLE
        var b = ns.qualifiedName("ex","b",factory);
        var bundle = factory.newNamedBundle(b,ns2,new ArrayList<>());
        bundle.getStatement().add(entity2);
        document.getStatementOrBundle().add(bundle);
        return document;
    }
}
