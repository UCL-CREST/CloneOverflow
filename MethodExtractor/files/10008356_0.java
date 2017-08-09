java.util.Random random = new Random();
boolean[] r_occupied;
boolean[] c_occupied;
for ( i = 0; i < vowels.length; i++ ) {
    r_occupied = new boolean[5];
    c_occupied = new boolean[5];
    count = random.nextInt ( 5 );
    for ( j = 0; j < count; j++ ) {
        row = random.nextInt ( 5 );
        while ( r_occupied[row] ) {
            row = ( row + 1 ) % 5;
        }
        col = random.nextInt ( 5 );
        while ( c_occupied[col] ) {
            col = ( col + 1 ) % 5;
        }
        r_occupied[row] = true;
        c_occupied[col] = true;
        board[row][col] = vowel[i];
    }
}
