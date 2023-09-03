package org.example;

import org.openprovenance.prov.interop.InteropFramework;


public class DateTimeMicroseconds {
    public static void perform() {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile("datetime_microseconds.provn");
        inf.writeDocument("datetime_microseconds.provn",document);

    }
}
