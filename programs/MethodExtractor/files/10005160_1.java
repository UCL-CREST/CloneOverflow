ArrayList<Object> maxKeys = new ArrayList<Object>();
Double maxValue = Double.MIN_VALUE;
for ( Map.Entry<Object, Double> entry : table.entrySet() ) {
    if ( entry.getValue() > maxValue ) {
        maxKeys.clear();
        maxKeys.add ( entry.getKey() );
        maxValue = entry.getValue();
    } else if ( entry.getValue() == maxValue ) {
        maxKeys.add ( entry.getKey() );
    }
}
