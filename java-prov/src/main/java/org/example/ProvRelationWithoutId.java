package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.ProvFactory;
import org.openprovenance.prov.vanilla.Document;


public class ProvRelationWithoutId {
    public static void perform() {
       var inf = new InteropFramework();
       var document = inf.readDocumentFromFile("data/prov_relation_without_id.json");
       inf.writeDocument("temp.provn",document);

    }
}
