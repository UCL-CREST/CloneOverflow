DIR=$1
TOOL=$2
PREFIX=$3
GCF=../tools/gcfFileConverter-0.4.jar

for i in $DIR/*.txt; do
	echo $i
	java -jar $GCF $TOOL $PREFIX $i
done   
