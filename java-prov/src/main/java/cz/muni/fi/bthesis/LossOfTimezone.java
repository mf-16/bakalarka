package cz.muni.fi.bthesis;

import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;
import java.util.ArrayList;


public class LossOfTimezone extends TestCase {

    public LossOfTimezone() {
        setFilename("loss_of_timezone");
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
            firstXmlGregorianCalendar = datatypeFactory.newXMLGregorianCalendar("2023-09-08T14:12:45.109-04:00");
            secondXmlGregorianCalendar1 = datatypeFactory.newXMLGregorianCalendar("2023-09-08T14:12:45.109+04:00");
        } catch (DatatypeConfigurationException e) {
            e.printStackTrace();
        }

        var activity = factory.newActivity(a, firstXmlGregorianCalendar, secondXmlGregorianCalendar1, new ArrayList<>());
        document.getStatementOrBundle().add(activity);
        document.setNamespace(ns);
        return document;
    }
}
