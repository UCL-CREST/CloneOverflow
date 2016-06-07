package eu.giuswhite.utils;

/**
 * Created by GiusWhite on 21/01/2016.
 */
public class CommonUtils {
    public static final String EXTRACTED_DATA_FOLDER_PATH = "";
    public static final String PROJECT_FOLDER_PATH = "/Users/Chaiyong/IdeasProjects/StackAnalyzer";
    public static final boolean TEST_MODE = true;
    public static int STOP_PROCESS_FLAG = 10;
    public static final String OPEN_CODE_PATTERN = "<pre><code>";
    public static final String CLOSED_CODE_PATTERN = "</code></pre>";
    public static final String CODE_LINES_STAT_CSV_HEADER = "# of lines, # of posts";
    public static final String stackoverflow_path = "stackoverflow_formatted/";
    public static final String SF_FRAG_LOCATION = "/Users/Chaiyong/Documents/stackoverflow/stackoverflow_formatted";
    public static final String qualitas_path = "src/";

    public static boolean isError(String fragId) {
        // 16327677_0.java
        // 25018225_0.java
        // 21535828_0.java
        // 22041769_1.java
        // "12124636_0.java"
        // "21655588_0.java"
        //if (fragId.contains("16327677_0.java") || fragId.contains("25018225_0.java")
        //        || fragId.contains("21535828_0.java") || fragId.contains("22041769_1.java")
        //        || fragId.contains("12124636_0.java") || fragId.contains("21655588_0.java")) {
        //    return true;
        //} else
        //    return false;
        return false;
    }
}
