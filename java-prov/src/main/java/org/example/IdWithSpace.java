package org.example;

import org.openprovenance.prov.interop.InteropFramework;


public class IdWithSpace {
    public static void perform() {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile("id_with_space.provn");
        inf.writeDocument("temp.provn",document);




        //BadUri.perform();
        WeirdCharacterAsIdentifier.perform();
    }
}
