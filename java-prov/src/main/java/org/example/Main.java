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
import java.io.Console;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Collection;
import java.util.GregorianCalendar;
import java.util.HashMap;
import java.util.List;


public class Main {
    public static void main(String[] args) {
//        InteropFramework inf = new InteropFramework();
//        ProvFactory factory = new org.openprovenance.prov.vanilla.ProvFactory();
//        var document = new org.openprovenance.prov.vanilla.Document();
//        var ns = new Namespace();
//        ns.addKnownNamespaces();
//        ns.registerDefault("http://purl.org/dc/terms/");
//        ns.register("ex", "https://example.org");
//        ns.register("dct", "http://purl.org/dc/terms/");
//        var ns2 = new Namespace();
//        ns2.addKnownNamespaces();
//
////
//
//
//        var eqn = ns.qualifiedName("ex", "1", factory);
//        var aqn = ns.qualifiedName("ex", "2", factory);
//        var tmp = ns.qualifiedName("dct", "hasPart", factory);
//        Collection<Attribute> attributes = new ArrayList<>();
//        attributes.add(factory.newAttribute(tmp, "attr_value", factory.getName().XSD_STRING));
//        Entity entity = factory.newEntity(eqn, attributes);
//        Activity activity = factory.newActivity(aqn);
//        WasGeneratedBy generatedBy = factory.newWasGeneratedBy(null, aqn, aqn);
//
////        BUNDLE
////        var bqn = ns.qualifiedName("ex","3",factory);
////        Collection<Statement> s = new ArrayList<>();
////        s.add(generatedBy);
////        var bundle = factory.newNamedBundle(bqn,s);
////        document.getStatementOrBundle().add(bundle);
////        bundle.setNamespace(ns2);
//
//        document.getStatementOrBundle().add(entity);
//        document.getStatementOrBundle().add(activity);
//        document.getStatementOrBundle().add(generatedBy);
//        entity.setId(aqn);
//
//        document.setNamespace(ns);
//        generatedBy.setId(aqn);
//
////        var inf = new InteropFramework();
////        var document = inf.readDocumentFromFile("data/java_temp.json");
//        inf.writeDocument("data/java_temp.provn", document);
//
//        File file = new File("data/java_temp.xml");
//        try {
//            OutputStream outputStream = new FileOutputStream(file);
//            inf.writeDocument(outputStream, Formats.ProvFormat.XML, document);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
        var bu = new BadUri();
        var dtm = new DateTimeMicroseconds();
        var iws = new IdWithSpace();
        var ir = new InvalidRecords();
        var jsn = new JsonDefaultNamespace();
        var pbatin = new ProvnBundleAndTopInstanceNamespace();
        var prwi = new ProvRelationWithoutId();
        var pv = new ProvValue();
        var wchai = new WeirdCharacterAsIdentifier();
        var hm = new HashMap<String,TestCase>();
        hm.put("bad_uri",bu);
        hm.put("datetime_microseconds",dtm);
        hm.put("id_with_space",iws);
        hm.put("invalid_records",ir);
        hm.put("json_default_namespace",jsn);
        hm.put("provn_bundle_and_top_instance_namespace",pbatin);
        hm.put("prov_relation_without_id",prwi);
        hm.put("prov_value",pv);
        hm.put("weird_character_as_identifier",wchai);
        if ("s".equals(args[2])){
            hm.get(args[0]).serialize(args[1]);
        }
        else if ("d".equals(args[2])){
            hm.get(args[0]).deserialize(args[1]);
        }
        //WeirdCharacterAsIdentifier.perform();
        //BadDate.perform();
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
