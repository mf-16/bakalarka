package org.example;

import org.openprovenance.prov.interop.Formats;
import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.*;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.ProvFactory;
import org.openprovenance.prov.model.QualifiedName;
import org.openprovenance.prov.model.Used;
import org.openprovenance.prov.model.WasGeneratedBy;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collection;
import java.util.GregorianCalendar;
import java.util.List;


public class Main {
    public static void main(String[] args) {
        InteropFramework inf = new InteropFramework();
        ProvFactory factory = new org.openprovenance.prov.vanilla.ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.registerDefault("default");
        ns.register("ex", "https://example.org");
        ns.register("ex", "https://example.org");
        var ns2 = new Namespace();
        ns2.addKnownNamespaces();

//


        var eqn = ns.qualifiedName("ex", "1", factory);
        var aqn = ns.qualifiedName("ex", "2", factory);
        Entity entity = factory.newEntity(eqn);
        Activity activity = factory.newActivity(aqn);
        WasGeneratedBy generatedBy = factory.newWasGeneratedBy(null, aqn, aqn);

//        BUNDLE
//        var bqn = ns.qualifiedName("ex","3",factory);
//        Collection<Statement> s = new ArrayList<>();
//        s.add(generatedBy);
//        var bundle = factory.newNamedBundle(bqn,s);
//        document.getStatementOrBundle().add(bundle);
//        bundle.setNamespace(ns2);

        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(activity);
        document.getStatementOrBundle().add(generatedBy);
        entity.setId(aqn);

        document.setNamespace(ns);
        generatedBy.setId(aqn);

//        var inf = new InteropFramework();
//        var document = inf.readDocumentFromFile("data/java_temp.json");
        inf.writeDocument("data/temp.provn", document);

//        File file = new File("data/java_temp.json");
//        try {
//            OutputStream outputStream = new FileOutputStream(file);
//            inf.writeDocument(outputStream, Formats.ProvFormat.JSON, document);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }


        //BadUri.perform();
        //WeirdCharacterAsIdentifier.perform();
        //IdWithSpace.perform();
        //DateTimeMicroseconds.perform();
        //InvalidRecords.perform();
        //ProvValue.perform();
        //JavaSerializationProblems.perform();
        //JsonDefaultNamespace.perform();
        //ProvnBundleAndTopInstanceNamespace.perform();
        //ProvRelationWithoutId.perform();

    }
}
