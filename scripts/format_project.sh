while read line           
do
	cd $line
	../../scripts/format_all.sh
  	cd ..      
done < $1
