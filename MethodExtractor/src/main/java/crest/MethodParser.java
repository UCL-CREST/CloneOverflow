package crest;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class MethodParser {
    private ArrayList<String> methodList = new ArrayList<>();
    private String FILE_PATH = "";

    public MethodParser(String filePath, String prefixToRemove) {
        FILE_PATH = filePath;
    }

    /***
     * Extract both methods and constructors
     * @return a list of methods & constructors
     */
    public ArrayList<String> parseMethods() {
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
                System.out.println("Unparseable method (use whole fragment)");
                String content = new Scanner(new File(FILE_PATH)).useDelimiter("\\Z").next();

                methodList.add(content);
            } finally {
                in.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return methodList;
    }

    /***
     * Extract methods
     */
    private class MethodVisitor extends VoidVisitorAdapter {
        @Override
        public void visit(MethodDeclaration n, Object arg) {

            List<Parameter> parameterArrayList = n.getParameters();
            // http://stackoverflow.com/questions/9205988/writing-a-java-program-to-remove-the-comments-in-same-java-program
            methodList.add(n.toStringWithoutComments());
            super.visit(n, arg);
        }
    }

    /***
     * Extract constructors
     */
    private class ConstructorVisitor extends VoidVisitorAdapter {
        @Override
        public void visit(ConstructorDeclaration c, Object arg) {
            methodList.add(c.toStringWithoutComments());
            super.visit(c, arg);
        }
    }
}
