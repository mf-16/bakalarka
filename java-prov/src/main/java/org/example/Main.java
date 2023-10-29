package org.example;

import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Method;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

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
//        args = new String[3];
//        args[0] = "test_test_case";
//        args[1] = "provn";
//        args[2] = "d";
//        var hm = new HashMap<String,TestCase>();
//        hm.put("checking_uri_syntax",new CheckingUriSyntax());
//        hm.put("loss_of_microseconds",new LossOfMicroseconds());
//        hm.put("local_part_of_id_with_space",new LocalPartOfIdWithSpace());
//        hm.put("nonsense_prov_records",new NonsenseProvRecords());
//        hm.put("default_namespace",new DefaultNamespace());
//        hm.put("top_instance_namespace_bundle",new TopInstanceNamespaceBundle());
//        hm.put("prov_record_without_id",new ProvRecordWithoutId());
//        hm.put("multiple_prov_value",new MultipleProvValue());
//        hm.put("escaped_characters",new EscapedCharacters());
//        hm.put("loss_of_timezone",new LossOfTimezone());
//        hm.put("prov_value_not_in_entity",new ProvValueNotInEntity());
//        hm.put("space_in_prefix",new SpaceInPrefix());
//        if ("s".equals(args[2])){
//            hm.get(args[0]).serialize(args[1]);
//        }
//        else if ("d".equals(args[2])){
//            hm.get(args[0]).deserialize(args[1]);
//        }
        var config = loadConfig();
        var key = config.getAsJsonObject(args[0]);
        var javaClass = key.get("java_class").getAsString();

        try {
            Class<?> clazz = Class.forName(javaClass);
            Object instance = clazz.getDeclaredConstructor().newInstance();
            Method method = null;
            if ("s".equals(args[2])){
                 method = clazz.getMethod("serialize",String.class);
            }
            else if ("d".equals(args[2])){
                 method = clazz.getMethod("deserialize",String.class);
            }
            method.invoke(instance,args[1]);
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("Error running Java class: " + e.getMessage());
        }
    }
    private static JsonObject loadConfig() {
        try (FileReader reader = new FileReader("../config.json")) {
            return JsonParser.parseReader(reader).getAsJsonObject();
        } catch (IOException e) {
            System.err.println("Error loading the configuration file: " + e.getMessage());
            return new JsonObject();
        }
    }

}
