package org.example;

import org.openprovenance.prov.interop.InteropFramework;


public class WeirdCharacterAsIdentifier {
    public static void perform() {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile("weird_char_as_id.provn");
        inf.writeDocument("temp.provn",document);




        //BadUri.perform();
    }
}
