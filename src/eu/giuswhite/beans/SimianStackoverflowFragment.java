package eu.giuswhite.beans;

import eu.giuswhite.utils.CommonUtils;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * Created by GiusWhite on 22/03/2016.
 */
public class SimianStackoverflowFragment {
    public String fragmentName;
    public int numberOfTimeIsUsed;
    public HashMap<Integer, Boolean> projectsWhereIsUsed;
    public boolean[] cloneLines;
    public int cloneLinesCount;
    public int SLOC;

    public SimianStackoverflowFragment(){
        this.numberOfTimeIsUsed = 0;
        this.projectsWhereIsUsed = new HashMap<>();
        this.cloneLinesCount = 0;
    }

    public SimianStackoverflowFragment(String filePath){
        this.numberOfTimeIsUsed = 0;
        this.projectsWhereIsUsed = new HashMap<>();
        try {
            this.setSLOC(filePath);
        } catch (IOException e) {
            System.err.println("Error: cannot read the file.");
            e.printStackTrace();
        }
    }

    public void setCloneLines(int start, int end) {
        for (int i = start - 1; i < end; i++)
            cloneLines[i] = true;
    }

    public void increaseCloneLinesCount(int size) {
        this.cloneLinesCount += size;
    }

    public int getCloneLinesCount() {
        return this.cloneLinesCount;
    }

    public int getCloneLines() {
        int count = 0;
        for (boolean isCloned: cloneLines) {
            if (isCloned)
                count++;
        }
        return count;
    }

    public void setSLOC(String filePath) throws IOException {
        SLOC = countLines(CommonUtils.SF_FRAG_LOCATION + "/" + filePath);
        // initiate the clone line array as well
        cloneLines = new boolean[SLOC];
    }

    public int getSLOC() {
        return SLOC;
    }

    /*** Copied from http://stackoverflow.com/questions/453018/number-of-lines-in-a-file-in-java **/
    public static int countLines(String filename) throws IOException {
        InputStream is = new BufferedInputStream(new FileInputStream(filename));
        try {
            byte[] c = new byte[1024];
            int count = 0;
            int readChars = 0;
            boolean empty = true;
            while ((readChars = is.read(c)) != -1) {
                empty = false;
                for (int i = 0; i < readChars; ++i) {
                    if (c[i] == '\n') {
                        ++count;
                    }
                }
            }
            return (count == 0 && !empty) ? 1 : count;
        } finally {
            is.close();
        }
    }
}
