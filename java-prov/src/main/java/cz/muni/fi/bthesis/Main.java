package cz.muni.fi.bthesis;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.openprovenance.prov.interop.InteropFramework;
import org.openprovenance.prov.model.Namespace;
import org.openprovenance.prov.model.QualifiedName;
import org.openprovenance.prov.vanilla.ProvFactory;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Method;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) {
        args = new String[3];
        args[0] = "prov_value_not_in_entity";
        args[1] = "xml";
        args[2] = "d";
        var config = loadConfig();
        var javaClass = "cz.muni.fi.bthesis." + config.get(args[0]).getAsString();

        try {
            Class<?> clazz = Class.forName(javaClass);
            Object instance = clazz.getDeclaredConstructor().newInstance();
            Method method = null;
            if ("s".equals(args[2])) {
                method = clazz.getMethod("serialize", String.class);
            } else if ("d".equals(args[2])) {
                method = clazz.getMethod("deserialize", String.class);
            }
            method.invoke(instance, args[1]);
        } catch (Exception e) {
            throw new RuntimeException("Error running Java class", e);
        }
    }

    private static JsonObject loadConfig() {
        Path configFilePath = Paths.get("..","config.json");
        try (FileReader reader = new FileReader(configFilePath.toFile())) {
            return JsonParser.parseReader(reader).getAsJsonObject();
        } catch (IOException e) {
            System.err.println("Error loading the configuration file: " + e.getMessage());
            return new JsonObject();
        }
    }

}
