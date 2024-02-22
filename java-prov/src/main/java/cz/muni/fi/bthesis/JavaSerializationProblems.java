package cz.muni.fi.bthesis;

import org.openprovenance.prov.interop.Formats;
import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;


public class JavaSerializationProblems {
    public static void perform() {
        ProvFactory factory = new org.openprovenance.prov.vanilla.ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.registerDefault("default");
        ns.register("ex", "https://example.org");
        var eqn = ns.qualifiedName("ex", "entity", factory);
        Entity entity = factory.newEntity(eqn);
        var qn = ns.qualifiedName("xsd", "string", factory);
        entity.setValue(factory.newValue(1, qn));
        document.getStatementOrBundle().add(entity);
        document.setNamespace(ns);


        var inf = new InteropFramework();

        //inf.writeDocument("../python-prov/java_temp.provn",document);

        File file = new File("../python-prov/java_serialization_problems.xml");
        try {
            OutputStream outputStream = new FileOutputStream(file);
            //inf.writeDocument(outputStream, Formats.ProvFormat.XML, document);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
