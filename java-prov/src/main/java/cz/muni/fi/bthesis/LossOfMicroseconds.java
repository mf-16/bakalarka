package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;
import java.util.ArrayList;


public class LossOfMicroseconds extends TestCase {
    public LossOfMicroseconds() {
        setFilename("loss_of_microseconds");
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
