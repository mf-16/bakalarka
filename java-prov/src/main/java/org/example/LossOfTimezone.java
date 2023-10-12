package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;
import java.util.ArrayList;


public class LossOfTimezone implements TestCase {

    public void serialize(String format) {
        var factory = new ProvFactory();
        var document = new Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex", "https://example.org");
        var eqn = ns.qualifiedName("ex", "a", factory);


        XMLGregorianCalendar firstXmlGregorianCalendar = null;
        XMLGregorianCalendar secondXmlGregorianCalendar1 = null;
        try {
            DatatypeFactory datatypeFactory = DatatypeFactory.newInstance();
            firstXmlGregorianCalendar = datatypeFactory.newXMLGregorianCalendar("2023-09-08T14:12:45.109-04:00");
            secondXmlGregorianCalendar1 = datatypeFactory.newXMLGregorianCalendar("2023-09-08T14:12:45.109+04:00");
        } catch (DatatypeConfigurationException e) {
            e.printStackTrace();
        }

        var activity = factory.newActivity(eqn, firstXmlGregorianCalendar, secondXmlGregorianCalendar1, new ArrayList<>());
        document.getStatementOrBundle().add(activity);
        document.setNamespace(ns);

        writeDocument(format,document,"loss_of_timezone");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/loss_of_timezone.%s", format));
        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }
}
