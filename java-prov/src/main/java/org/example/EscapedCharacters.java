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


public class EscapedCharacters extends TestCase {
    public EscapedCharacters(){
        setFilename("escaped_characters");
    }

    @Override
    public Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org/");
        var e = ns.qualifiedName("ex","='(),-:;[].",factory);
        Entity entity = factory.newEntity(e);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        return document;
    }
}
