package org.example;

import com.google.gson.JsonSerializer;
import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.*;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.ProvFactory;
import org.openprovenance.prov.model.QualifiedName;
import org.openprovenance.prov.model.Used;
import org.openprovenance.prov.model.WasGeneratedBy;
import org.openprovenance.prov.xml.*;
import org.openprovenance.prov.xml.Document;
import org.openprovenance.prov.xml.ProvSerialiser;

import org.openprovenance.prov.json.ProvDocumentSerializer;

import javax.xml.bind.JAXBException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;


public class Main {
    public static void main(String[] args) {
//        var inf = new InteropFramework();
//        ProvFactory factory = InteropFramework.newXMLProvFactory();
//        var document = new Document();
//        var ns = new Namespace();
//        ns.addKnownNamespaces();
//        var eqn = ns.qualifiedName("prov","entity",factory);
//        var aqn = ns.qualifiedName("prov","activity",factory);
//        Entity entity = factory.newEntity(eqn);
//        Activity activity = factory.newActivity(aqn);
//        WasGeneratedBy generatedBy = factory.newWasGeneratedBy(ns.qualifiedName("prov","1",factory),eqn,aqn);
//        document.getStatementOrBundle().add(entity);
//        document.getStatementOrBundle().add(activity);
//        document.getStatementOrBundle().add(generatedBy);
//        document.setNamespace(ns);
//        var inf = new InteropFramework();
//        var document = inf.readDocumentFromFile("temp.provn");
//        inf.writeDocument("java_temp.dot",document);




        //BadUri.perform();
        //WeirdCharacterAsIdentifier.perform();
        //IdWithSpace.perform();
        //DateTimeMicroseconds.perform();

    }
}
