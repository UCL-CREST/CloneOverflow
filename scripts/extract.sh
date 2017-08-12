while read line           
do
	foldername=`echo $line | cut -d'.' -f1`
	echo $foldername 
	mkdir $foldername
        cp ../compressed_src/$line $foldername 
	cd $foldername

        if [ ${line: -4} == ".jar" ]
        then
            mv $line `echo $line | sed 's/\(.*\.\)jar/\1zip/'`
            unzip $line
        elif [ ${line: -4} == ".zip" ]
            then
            unzip $line 
        elif [ ${line: -3} == ".gz" ]
            then
            tar -zxvf $line
        fi
	rm *.zip *.jar *.gz	
  	cd ..      
done < $1
