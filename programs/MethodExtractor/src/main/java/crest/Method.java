package crest;

public class Method {
    private String code;
    private int start;
    private int end;

    public Method(String code, int start, int end) {
        this.code = code;
        this.start = start;
        this.end = end;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }

    public int getEnd() {
        return end;
    }

    public void setEnd(int end) {
        this.end = end;
    }
}
