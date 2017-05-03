import java.io.*;
import java.util.*;

/**
 * Created by Chaiyong on 5/2/17.
 */
public class Main {
    public static void main(String[] args) {
//        File file = new File("clones.csv");
        File file = new File("clones_qs_ex_ud.csv");
        HashMap<String, HashSet<String>> cloneMap = new HashMap<String ,HashSet<String>>();
        HashMap<String, HashSet<String>> cloneMapNoLine = new HashMap<String ,HashSet<String>>();

        HashSet<String> snippets;
        HashSet<String> snippetsNoLine;

        int count = 0;
        // copied from
        // http://stackoverflow.com/questions/5868369/how-to-read-a-large-text-file-line-by-line-using-java
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;

            while ((line = br.readLine()) != null) {
                if (line.contains(",")) {
                    count++;
                    String[] lineSplit = line.split(",");

                    String qClone = "";
                    String qCloneNoLine = "";
                    String soClone = "";
                    String soCloneNoLine = "";

                    if (lineSplit.length >= 11) {
                        qClone = lineSplit[3] + "$"
                                + lineSplit[4] + "$"
                                + lineSplit[5] + "$"
                                + lineSplit[9] + "$"
                                + lineSplit[10] + "$"
                                + lineSplit[11];
                        soClone = lineSplit[0] + "$"
                                + lineSplit[1] + "$"
                                + lineSplit[2] + "$"
                                + lineSplit[6] + "$"
                                + lineSplit[7] + "$"
                                + lineSplit[8];
                    } else {
                        qClone = lineSplit[3] + "$"
                                + lineSplit[4] + "$"
                                + lineSplit[5];

                        soClone = lineSplit[0] + "$"
                                + lineSplit[1] + "$"
                                + lineSplit[2];
                    }
                    qCloneNoLine = lineSplit[3];
                    soCloneNoLine = lineSplit[0];

                    if (cloneMap.get(qClone) == null) {
                        snippets = new HashSet<String>();
                        snippets.add(soClone);
                    } else {
                        snippets = cloneMap.get(qClone);
                        snippets.add(soClone);
                    }

                    if (cloneMapNoLine.get(qCloneNoLine) == null) {
                        snippetsNoLine = new HashSet<String>();
                        snippetsNoLine.add(soCloneNoLine);
                    } else {
                        snippetsNoLine = cloneMapNoLine.get(qCloneNoLine);
                        snippetsNoLine.add(soCloneNoLine);
                    }

                    cloneMap.put(qClone, snippets);
                    cloneMapNoLine.put(qCloneNoLine, snippetsNoLine);
                }
            }

            int totalQClones = cloneMap.size();
            int totalQCloneNoLine = cloneMapNoLine.size();
            int totalCount = 0;

            Iterator it = cloneMapNoLine.entrySet().iterator();

            while (it.hasNext()) {
                Map.Entry pair = (Map.Entry) it.next();
                HashSet<String> tmpSnippets = (HashSet<String>) pair.getValue();
                totalCount += tmpSnippets.size();
                it.remove(); // avoids a ConcurrentModificationException
            }

            System.out.println("----------------");

            System.out.println("No. of distinct Qualitas file: " + totalQCloneNoLine + " out of " + count + " clone pairs.");
            System.out.println("Average SO snippets per a Qualitas file: " + ((double) totalCount) / totalQCloneNoLine);

            it = cloneMap.entrySet().iterator();
            totalCount = 0;
            int snippetPerQCount = 0;

            while (it.hasNext()) {
                Map.Entry pair = (Map.Entry) it.next();
                HashSet<String> tmpSnippetsWithLines = (HashSet<String>) pair.getValue();
                totalCount += tmpSnippetsWithLines.size();
                it.remove(); // avoids a ConcurrentModificationException
            }

            System.out.println("----------------");
            System.out.println("No. of distinct Qualitas clones: " + totalQClones + " out of " + count + " clone pairs.");
            System.out.println("Average SO clones per a Qualitas clone: " + ((double) totalCount)/totalQClones);

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
