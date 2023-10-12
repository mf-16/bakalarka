package org.example;

import org.apache.commons.collections4.collection.TransformedCollection;
import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.*;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.util.ArrayList;


public class NonsenseProvRecords implements TestCase {

    public void serialize(String format) {
        var factory = new ProvFactory();
        var document = new org.openprovenance.prov.vanilla.Document();
        var ns = new Namespace();
        ns.addKnownNamespaces();
        ns.register("ex","https://example.org");
        var e = ns.qualifiedName("ex","e",factory);
        var c = ns.qualifiedName("ex","c",factory);
        var provqn = ns.qualifiedName("prov","QUALIFIED_NAME",factory);
        var ac = ns.qualifiedName("ex","ac",factory);
        var ag = ns.qualifiedName("ex","ag",factory);
        Entity entity = factory.newEntity(e);
        Activity activity = factory.newActivity(ac);
        Agent agent = factory.newAgent(ag);
        WasGeneratedBy wasGeneratedBy = factory.newWasGeneratedBy(null,ag,e);
        Used used = factory.newUsed(null,ag,ac);
        WasInformedBy wasInformedBy = factory.newWasInformedBy(null,e,e);
        WasStartedBy wasStartedBy = factory.newWasStartedBy(null,e,ag,ac);
        WasEndedBy wasEndedBy = factory.newWasEndedBy(null,e,ag,ac);
        WasInvalidatedBy wasInvalidatedBy = factory.newWasInvalidatedBy(null,ag,e);
        WasDerivedFrom wasDerivedFrom = factory.newWasDerivedFrom(null,ac,ag,e,e,ag,new ArrayList<>());
        WasAttributedTo wasAttributedTo = factory.newWasAttributedTo(null,ac,ac);
        WasAssociatedWith wasAssociatedWith = factory.newWasAssociatedWith(null,e,e);
        ActedOnBehalfOf actedOnBehalfOf = factory.newActedOnBehalfOf(null,e,ac);
        WasInfluencedBy wasInfluencedBy = factory.newWasInfluencedBy(null,ag,ac);
        AlternateOf alternateOf = factory.newAlternateOf(ag, ac);
        SpecializationOf specializationOf = factory.newSpecializationOf(e,ac);
        Entity collection = factory.newEntity(c);
        collection.getType().add(factory.newType("prov:Collection",provqn));
        factory.newHadMember(c,ag);
        factory.newHadMember(c,ac);





        document.getStatementOrBundle().add(entity);
        document.getStatementOrBundle().add(activity);
        document.getStatementOrBundle().add(agent);
        document.getStatementOrBundle().add(wasGeneratedBy);
        document.getStatementOrBundle().add(used);
        document.getStatementOrBundle().add(wasInformedBy);
        document.getStatementOrBundle().add(wasStartedBy);
        document.getStatementOrBundle().add(wasEndedBy);
        document.getStatementOrBundle().add(wasInvalidatedBy);
        document.getStatementOrBundle().add(wasDerivedFrom);
        document.getStatementOrBundle().add(wasAttributedTo);
        document.getStatementOrBundle().add(wasAssociatedWith);
        document.getStatementOrBundle().add(actedOnBehalfOf);
        document.getStatementOrBundle().add(wasInfluencedBy);
        document.getStatementOrBundle().add(alternateOf);
        document.getStatementOrBundle().add(specializationOf);
        document.getStatementOrBundle().add(collection);

        document.setNamespace(ns);

        writeDocument(format,document,"nonsense_prov_records");
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        Document document = inf.readDocumentFromFile(String.format("data/nonsense_prov_records.%s", format));
        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }
}
