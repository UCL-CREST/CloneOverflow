while IFS='' read -r line || [[ -n "$line" ]]; do
    #echo "Text read from file: $line"
    size=`echo $line | cut -d',' -f9 | cut -d'.' -f1`
    #echo $size
    if [ $size -gt 10 ]; then
        echo $line
    fi
done < "$1"
