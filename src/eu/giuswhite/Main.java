package eu.giuswhite;

import org.apache.commons.cli.*;

import java.io.File;

public class Main {
    private static Options options = new Options();
    private static String fileDir;

    public static void main(String[] args) {
        processCommandLine(args);
//        ParserManager.getInstance().stackoverflowParser();
//        Map map = LineCounter.getInstance().getMapOfLinesStat(CommonUtils.PROJECT_FOLDER_PATH + "\\data_four_split\\0\\");
//        Map smallest = LineCounter.getInstance().getTopSmallestFile();
//        Map biggest = LineCounter.getInstance().getTopBiggestFile();
//        CsvFileWriter.sortHashMapByKey("first_half_stats", CommonUtils.CODE_LINES_STAT_CSV_HEADER, map);
//        CsvFileWriter.writeHashMapToCsv("Post ID, # of lines", smallest, "first_half_5_smallest_code");
//        CsvFileWriter.writeHashMapToCsv("Post ID, # of lines", biggest, "first_half_5_sbiggest_code");

       /* Map map = new HashMap<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            System.out.println("Path of projects folder:");
            String path = br.readLine();
            System.out.println("Destination path:");
            String destinatioPath = br.readLine();
            System.out.println("Result file name:");
            String resultFileName = br.readLine();
            FileManager.getDirectoryContents(new File(path), map);
            map = FileManager.randomizeMap(map);
            CsvFileWriter.writeHashMapToCsv(destinatioPath,"File Name, File Path", map, resultFileName);

        } catch (IOException e) {
            e.printStackTrace();
        }*/
        String gcfDir = fileDir;
        File f = new File(gcfDir);
        if (f.exists() && f.isDirectory()) {
            ParserManager.getInstance().simianLogsFilterParser(gcfDir);
        } else {
            System.err.println("Error: the given directory " + gcfDir + " does not exist.");
        }
        // ParserManager.getInstance().usefulSimianFragmentStatisticParser();
    }

    private static void processCommandLine(String[] args) {
        // create the command line parser
        CommandLineParser parser = new DefaultParser();

        options.addOption("d", "dir", true, "File's directory");
        options.addOption("h", "help", false, "Print help");

        // check if no parameter given, print help and quit
        if (args.length == 0) {
            showHelp();
            System.exit(0);
        }

        try {
            // parse the command line arguments
            CommandLine line = parser.parse(options, args);

            if (line.hasOption("h")) {
                showHelp();
            }

            if (line.hasOption("d")) {
                fileDir = line.getOptionValue("d");
            } else {
                showHelp();
                throw new ParseException("No file directory provided.");
            }
        } catch (ParseException exp) {
            System.out.println("Warning: " + exp.getMessage());
        }
    }

    private static void showHelp() {
        HelpFormatter formater = new HelpFormatter();
        formater.printHelp("(v 0.1) java -jar stackanalyzer.jar", options);
        System.exit(0);
    }
}
