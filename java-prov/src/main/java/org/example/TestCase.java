package org.example;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.vanilla.Document;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

/**
 * @author Matus Formanek
 */
public interface TestCase {
    void serialize(String format);
    void deserialize(String format);

    default void writeDocument(String format, Document document, String filename){
        var inf = new InteropFramework();
        var formatType = inf.getTypeForFormat(format);

        File file = new File(String.format("../python-prov/data/%s.%s", filename,format));
        try {
            OutputStream outputStream = new FileOutputStream(file);
            inf.writeDocument(outputStream, formatType, document);
            inf.writeDocument(System.out, formatType, document);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
