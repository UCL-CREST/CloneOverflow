package crest;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java -jar MethodExtract.jar <filename>");
        } else {
        /* delete the output file if it exist */
            File resultFile = new File("methods.txt");
            File zeroMethodFile = new File("zero_method.txt");
            if (resultFile.exists())
                resultFile.delete();
            if (zeroMethodFile.exists())
                zeroMethodFile.delete();

            String file = args[0];
            MethodParser mp = new MethodParser(file, "");
            ArrayList<String> methods = mp.parseMethods();

            if (methods.size() != 0) {
                for (int i = 0; i < methods.size(); i++) {
                    if (i == 0)
                        writeToFile("./", "methods.txt", methods.get(i), true);
                    else
                        writeToFile("./", "methods.txt", "\n@@==UCL==@@\n" + methods.get(i) + "\n", true);
                }
            } else {
                // can't extract any methods (something's wrong)
                writeToFile("./", "zero_method.txt", file + "\n", true);
            }
        }
    }

    public static void writeToFile(String location, String filename, String content, boolean isAppend) {
        if (createDir(location)) {
            /* copied from https://www.mkyong.com/java/how-to-write-to-file-in-java-bufferedwriter-example/ */
            BufferedWriter bw = null;
            FileWriter fw = null;

            try {
                fw = new FileWriter(location + "/" + filename, isAppend);
                bw = new BufferedWriter(fw);
                bw.write(content);
                if (!isAppend)
                    System.out.println("Saved as: " + filename);
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (bw != null)
                        bw.close();
                    if (fw != null)
                        fw.close();
                } catch (IOException ex) {
                    ex.printStackTrace();
                }

            }
        } else {
            System.out.println("ERROR: can't create a directory at: " + location);
        }
    }

    private static boolean createDir(String location) {
        try {
            Files.createDirectories(Paths.get(location));
        } catch (IOException e) {
            e.printStackTrace();
        }
        return true;
    }
}
