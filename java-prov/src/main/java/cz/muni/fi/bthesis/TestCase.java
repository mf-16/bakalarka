package cz.muni.fi.bthesis;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.vanilla.Document;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

/**
 * @author Matus Formanek
 */
public abstract class TestCase {
    private String filename;

    public void serialize(String format) {
        var document = createDocument();

        writeDocument(format, document, filename);
    }

    public void deserialize(String format) {
        var inf = new InteropFramework();
        var document = inf.readDocumentFromFile(String.format("data/%s.%s", filename, format));

        var expectedDocument = createDocument();
        System.out.println(document.equals(expectedDocument));

        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }

    public void writeDocument(String format, Document document, String filename) {
        var inf = new InteropFramework();
        var formatType = inf.getTypeForFormat(format);

        File file = new File(String.format("../python-prov/data/%s.%s", filename, format));
        try {
            OutputStream outputStream = new FileOutputStream(file);
            inf.writeDocument(outputStream, formatType, document);
            inf.writeDocument(System.out, formatType, document);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    abstract Document createDocument();

    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
}
