package crest;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;

import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Stream;

public class MethodParser {
    private ArrayList<Method> methodList = new ArrayList<>();
    private String FILE_PATH = "";

    public MethodParser(String filePath, String prefixToRemove) {
        FILE_PATH = filePath;
    }

    /***
     * Extract both methods and constructors
     * @return a list of methods & constructors
     */
    public ArrayList<Method> parseMethods() {
        try {
            FileInputStream in = new FileInputStream(FILE_PATH);
            CompilationUnit cu;
            try {
                cu = JavaParser.parse(in);

                List<TypeDeclaration> types = cu.getTypes();
                for (TypeDeclaration type : types) {
                    if (type instanceof ClassOrInterfaceDeclaration) {
                        // getting class name
                        ClassOrInterfaceDeclaration classDec = (ClassOrInterfaceDeclaration) type;
                    }
                }
                new ConstructorVisitor().visit(cu, null);
                new MethodVisitor().visit(cu, null);
            } catch (Throwable e) {
                readWholeFile();
            } finally {
                in.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        // finally, there's still no method extracted.
        // use the whole snippet.
        if (methodList.size() == 0) {
            readWholeFile();
        }

        return methodList;
    }

    /***
     * Extract methods
     */
    private class MethodVisitor extends VoidVisitorAdapter {
        @Override
        public void visit(MethodDeclaration n, Object arg) {
            // http://stackoverflow.com/questions/9205988/writing-a-java-program-to-remove-the-comments-in-same-java-program
            methodList.add(new Method(n.toStringWithoutComments(), n.getBeginLine(), n.getEndLine()));
            super.visit(n, arg);
        }
    }

    /***
     * Extract constructors
     */
    private class ConstructorVisitor extends VoidVisitorAdapter {
        @Override
        public void visit(ConstructorDeclaration c, Object arg) {
            methodList.add(new Method(c.toStringWithoutComments(), c.getBeginLine(), c.getEndLine()));
            super.visit(c, arg);
        }
    }

    private void readWholeFile() {
        try {
            System.out.println("Unparseable method (use whole fragment)");
            // String content = new Scanner(new File(FILE_PATH)).useDelimiter("\\Z").next();
            StringBuilder content = new StringBuilder();
            int numberOfLines = 0;
            /* example from here: https://www.leveluplunch.com/java/examples/count-number-of-lines-in-text-file/ */
            FileReader fr = new FileReader(FILE_PATH);
            BufferedReader br = new BufferedReader(fr);
            String line;
            while((line = br.readLine()) != null){
                content.append(line + "\n");
                numberOfLines++;
            }
            br.close();
            fr.close();
            methodList.add(new Method(content.toString(), 1, numberOfLines));
        } catch (FileNotFoundException e1) {
            System.out.println("File not found.");
        } catch (IOException e2) {
            e2.printStackTrace();
        }
    }
}
