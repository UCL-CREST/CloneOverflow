public void run() {
    boolean processing = true;
    while ( processing ) {
        try {
            byte[] buffer = new byte[8192];
            fis = new FileOutputStream ( "C:\\" + ( s1++ ) + ".jpg" );
            while ( ( count = in.read ( buffer ) ) > 0 ) {
                fis.write ( buffer, 0, count );
                fis.flush();
            }
            processing = false;
        } catch ( Exception e ) {
            processing = false;
        }
    }
}
