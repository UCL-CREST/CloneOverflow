import java.io.*;
import java.util.*;

/**
 * Created by Chaiyong on 5/2/17.
 */
public class Main {
    public static void main(String[] args) {
        File file = new File("clones.csv");
        HashMap<String, HashSet<String>> cloneMap = new HashMap<String ,HashSet<String>>();
        HashMap<String, HashSet<String>> cloneMapNoLine = new HashMap<String ,HashSet<String>>();

        HashSet<String> snippets;
        HashSet<String> snippetsNoLine;

        HashSet<String> qualitasClones = new HashSet<String>();
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
                    String soClone = "";

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

                    if (cloneMap.get(qClone) == null) {
                        snippets = new HashSet<String>();
                        snippetsNoLine = new HashSet<String>();

                        snippets.add(soClone);
                        snippetsNoLine.add(lineSplit[0]);
                    } else {
                        snippets = cloneMap.get(qClone);
                        snippetsNoLine = cloneMapNoLine.get(qClone);

                        snippets.add(soClone);
                        snippetsNoLine.add(lineSplit[0]);
                    }

                    cloneMap.put(qClone, snippets);
                    cloneMapNoLine.put(qClone, snippetsNoLine);
                }
            }

            int totalQClones = cloneMap.size();
            System.out.println("No. of distinct Qualitas clones: " + totalQClones + " out of " + count);

            int multipleSnippetsCounter = 0;
            int oneOneSnippetCounter = 0;
            int totalCount = 0;

            Iterator it = cloneMapNoLine.entrySet().iterator();

            while (it.hasNext()) {
                Map.Entry pair = (Map.Entry)it.next();
                HashSet<String> tmpSnippets = (HashSet<String>) pair.getValue();

                if (tmpSnippets.size() > 1)
                    multipleSnippetsCounter++;
                else
                    oneOneSnippetCounter++;

                totalCount += tmpSnippets.size();

                it.remove(); // avoids a ConcurrentModificationException
            }

            System.out.println("----------------");
            System.out.println("Multiple snippet: " + multipleSnippetsCounter);
            System.out.println("One snippet: " + oneOneSnippetCounter);
            System.out.println("Total snippet: " + totalCount);

            it = cloneMap.entrySet().iterator();
            totalCount = 0;
            int multipleSOSnippetCount = 0;
            int snippetPerQCount = 0;

            while (it.hasNext()) {
                Map.Entry pair = (Map.Entry)it.next();
                HashSet<String> tmpSnippetsWithLines = (HashSet<String>) pair.getValue();

                if (tmpSnippetsWithLines.size() > 1) {

                    HashSet<String> soSnippetSet = new HashSet<String>();
                     multipleSnippetsCounter++;

                    for (String so: tmpSnippetsWithLines) {
                        String[] tmp = so.split("\\$");
                        // check if there are multiple snippets
                        soSnippetSet.add(tmp[0]);
                    }

                    // System.out.println(soSnippetSet);

                    // if multiple snippets
                    if (soSnippetSet.size() > 1) {
                        multipleSOSnippetCount++;
                        snippetPerQCount += soSnippetSet.size();
                    }
                } else
                    oneOneSnippetCounter++;

                totalCount += tmpSnippetsWithLines.size();

                it.remove(); // avoids a ConcurrentModificationException
            }

            System.out.println("----------------");
            System.out.println("Multiple snippets per Q clone: " + multipleSnippetsCounter);
            System.out.println("Multiple 'unique' snippets per Q clone: " + multipleSOSnippetCount);
            System.out.println("Average SO snippets per Q clone: " + ((double) snippetPerQCount)/totalQClones);
            System.out.println("One snippet: " + oneOneSnippetCounter);
            System.out.println("Total snippets: " + totalCount);

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
