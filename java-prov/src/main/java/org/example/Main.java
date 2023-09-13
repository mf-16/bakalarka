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
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.GregorianCalendar;


public class Main {
    public static void main(String[] args) {
//        InteropFramework inf = new InteropFramework();
//        ProvFactory factory = new org.openprovenance.prov.vanilla.ProvFactory();
//        var document = new org.openprovenance.prov.vanilla.Document();
//        var ns = new Namespace();
//        ns.addKnownNamespaces();
//        ns.register("ex ex","exex");
//        var eqn = ns.qualifiedName("ex ex","entity",factory);
//        var aqn = ns.qualifiedName("prov","activity",factory);
//        Entity entity = factory.newEntity(eqn);
//        XMLGregorianCalendar xmlGregorianCalendar = null;
//        try {
//            // Create a DatatypeFactory instance
//            DatatypeFactory datatypeFactory = DatatypeFactory.newInstance();
//            GregorianCalendar currentCalendar = new GregorianCalendar();
//
//            // Create an XMLGregorianCalendar instance representing a specific date and time
//            xmlGregorianCalendar = datatypeFactory.newXMLGregorianCalendar(currentCalendar);
//            xmlGregorianCalendar.setTimezone(5);
//
//            // Print the XMLGregorianCalendar
//            System.out.println("XMLGregorianCalendar: " + xmlGregorianCalendar);
//        } catch (DatatypeConfigurationException e) {
//            throw new RuntimeException(e);
//        }
//        Activity activity = factory.newActivity(aqn,xmlGregorianCalendar,xmlGregorianCalendar,new ArrayList<>());
//        WasGeneratedBy generatedBy = factory.newWasGeneratedBy(ns.qualifiedName("prov","1",factory),eqn,aqn);
//        document.getStatementOrBundle().add(entity);
//        document.getStatementOrBundle().add(activity);
//        document.getStatementOrBundle().add(generatedBy);
//        document.setNamespace(ns);
//
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile("temp.provn");
        inf.writeDocument("java_temp.provn",document);
//        inf.writeDocument(System.out, Formats.ProvFormat.JSON, document);




        //BadUri.perform();
        WeirdCharacterAsIdentifier.perform();
        //IdWithSpace.perform();
        //DateTimeMicroseconds.perform();
        //InvalidRecords.perform();
        //ProvValue.perform();

    }
}
