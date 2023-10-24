package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;
import java.util.ArrayList;


public class LossOfMicroseconds implements TestCase {

    public void serialize(String format) {
        var document = createDocument();
        writeDocument(format,document,"loss_of_microseconds");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/loss_of_microseconds.%s", format));

        var expectedDocument = createDocument();
        System.out.println(document.equals(expectedDocument));

        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }

    @Override
    public Document createDocument() {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex", "https://example.org/");
        var a = ns.qualifiedName("ex", "a", factory);


        XMLGregorianCalendar firstXmlGregorianCalendar = null;
        XMLGregorianCalendar secondXmlGregorianCalendar1 = null;
        try {
            DatatypeFactory datatypeFactory = DatatypeFactory.newInstance();
            firstXmlGregorianCalendar = datatypeFactory.newXMLGregorianCalendar("2023-09-08T14:12:45.10931231236545213876");
            secondXmlGregorianCalendar1 = datatypeFactory.newXMLGregorianCalendar("2023-09-08T14:12:45.109321321312321432523");
        } catch (DatatypeConfigurationException ex) {
            ex.printStackTrace();
        }

        var activity = factory.newActivity(a, firstXmlGregorianCalendar, secondXmlGregorianCalendar1, new ArrayList<>());
        document.getStatementOrBundle().add(activity);
        document.setNamespace(ns);
        return document;
    }
}
