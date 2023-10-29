package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.HadMember;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.vanilla.Document;
import org.openprovenance.prov.vanilla.ProvFactory;

import javax.xml.datatype.DatatypeConfigurationException;
import javax.xml.datatype.DatatypeFactory;
import javax.xml.datatype.XMLGregorianCalendar;
import java.util.ArrayList;

/**
 * @author Matus Formanek
 */
public class TestTestCase implements TestCase{
    public void serialize(String format) {
        var document = createDocument();

        writeDocument(format,document,"test_test_case");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/test_test_case.%s", format));

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
        var e = ns.qualifiedName("ex", "e", factory);
        var col_id = ns.qualifiedName("ex", "c", factory);
        var col_prefix = ns.qualifiedName("prov", "Collection", factory);
        var provqn = ns.qualifiedName("prov","QUALIFIED_NAME",factory);
        Entity collection = factory.newEntity(col_id);
        Entity entity = factory.newEntity(e);
        collection.getType().add(factory.newType(col_prefix,provqn));
        HadMember hadMember = factory.newHadMember(col_id,e);
        document.getStatementOrBundle().add(collection);
        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(hadMember);
        document.setNamespace(ns);
        return document;
    }
}
