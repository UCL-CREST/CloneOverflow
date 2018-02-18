public void testStaticInit() throws Exception {
    try {
        new BadInitClass().doSomething();
    } catch ( Throwable t ) {
        assertThat ( t, instanceOf ( Error.class ) );
        assertThat (
            getFullStackTraceWithCauses ( t ),
            containsString ( "I need to see this message" ) );
    }
    try {
        new BadInitClass().doSomething();
    } catch ( Throwable t ) {
        assertThat ( t, instanceOf ( NoClassDefFoundError.class ) );
        assertThat (
            getFullStackTraceWithCauses ( t ),
            not ( containsString ( "I need to see this message" ) ) );
    }
}
private String getFullStackTraceWithCauses ( Throwable t ) {
    StringWriter writer = new StringWriter();
    t.printStackTrace ( new PrintWriter ( writer ) );
    return writer.toString();
}
