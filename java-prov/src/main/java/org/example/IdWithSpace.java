package org.example;

import org.openprovenance.prov.interop.InteropFramework;


public class IdWithSpace implements  TestCase {

    public void serialize(String format) {
        //TODO
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/id_with_space.%s", format));
    }
}
