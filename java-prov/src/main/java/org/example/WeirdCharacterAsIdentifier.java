package org.example;

import org.openprovenance.prov.interop.InteropFramework;


public class WeirdCharacterAsIdentifier implements TestCase {
    public void serialize(String format) {
        //TODO
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/weird_character_as_identifier.%s", format));
    }
}
