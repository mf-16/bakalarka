package org.example;

import org.openprovenance.prov.interop.Formats;
import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.Statement;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Collection;


public class ProvnBundleAndTopInstanceNamespace implements TestCase {
    public static void perform() {

    }

    public void serialize(String format) {
        ProvFactory factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org");
        var ns2 = new Namespace();
        ns2.addKnownNamespaces();
        var eqn = ns.qualifiedName("ex","entity",factory);
        Entity entity = factory.newEntity(eqn);
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);
        // BUNDLE
        var bqn = ns.qualifiedName("ex","3",factory);
        var bundle = factory.newNamedBundle(bqn,new ArrayList<>());
        document.getStatementOrBundle().add(bundle);
        bundle.setNamespace(ns2);


        var inf = new InteropFramework();
        var formatType = inf.getTypeForFormat(format);

        File file = new File(String.format("../python-prov/data/provn_bundle_and_top_instance.%s", format));
        try {
            OutputStream outputStream = new FileOutputStream(file);
            inf.writeDocument(outputStream, formatType , document);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/provn_bundle_and_top_instance.%s", format));
    }
}
