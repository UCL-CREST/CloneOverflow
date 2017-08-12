#!/bin/sh

for i in *; do
    cd $i
    for j in `find . -type f -name *.java`; do
	echo "*** ASTYLE $i/$j"
	/scratch0/NOT_BACKED_UP/crest/gbianco/tools/astyle --style=java -p -P -d -H -U -xd -j "$j"
	mv "$j" "$j~"
	echo "*** UNCOMMENT $j"
        /scratch0/NOT_BACKED_UP/crest/gbianco/tools/uncomment-java < "$j~"| sed -e '/^[ \t\r]*$/d' > "$j"
	if [ -f $j ]; then
	    rm "$j~" 
	fi
	if [ -f "$j.orig" ]; then
	    rm "$j.orig"
	fi	
    done
    cd ..
done
