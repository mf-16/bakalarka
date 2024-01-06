package cz.muni.fi.bthesis;

import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.vanilla.Document;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.nio.file.Path;
import java.nio.file.Paths;

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

        Path filePath = Paths.get("data", filename + "." + format);
        var document = inf.readDocumentFromFile(filePath.toString());

        var expectedDocument = createDocument();
        System.out.println(document.equals(expectedDocument));
        System.out.println("----------");
        var formatType = inf.getTypeForFormat(format);
        inf.writeDocument(System.out, formatType, document);
    }

    public void writeDocument(String format, Document document, String filename) {
        var inf = new InteropFramework();
        var formatType = inf.getTypeForFormat(format);

        Path filePath = Paths.get("..", "python-prov", "data", filename + "." + format);
        File file = filePath.toFile();
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
