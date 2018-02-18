Object maxKey = null;
Double maxValue = Double.MIN_VALUE;
for ( Map.Entry<Object, Double> entry : table.entrySet() ) {
    if ( entry.getValue() > maxValue ) {
        maxValue = entry.getValue();
        maxKey = entry.getKey();
    }
}
