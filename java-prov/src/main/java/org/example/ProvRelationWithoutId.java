package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.ProvFactory;
import org.openprovenance.prov.vanilla.Document;


public class ProvRelationWithoutId implements TestCase {

    public void serialize(String format) {
        //TODO
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/prov_relation_without_id.%s", format));
    }
}
