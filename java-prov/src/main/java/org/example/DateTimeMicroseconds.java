package org.example;

import org.openprovenance.prov.interop.InteropFramework;


public class DateTimeMicroseconds implements TestCase {

    public void serialize(String format) {
        //TODO
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/date_time_microseconds.%s", format));
    }
}
