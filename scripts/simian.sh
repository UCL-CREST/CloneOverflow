RAM_PROJECT_FOLDER=/dev/shm/cragkhit
SRC_SIMIAN_FOLDER=/dev/shm/cragkhit/src
FILES=/home/cragkhit/Documents/projects_130901r_pt1+2+3
SETTING=$2

echo "Reading from $1, analysing using settings $2"

for i in `ls $1`; do    
    printf "*** Processing: $FILES/$i ***\n"
    if [ ! -d $SRC_SIMIAN_FOLDER ]; then
        mkdir $SRC_SIMIAN_FOLDER
    fi
    if [ ! -d ${RAM_PROJECT_FOLDER}/simian_results ]; then
        mkdir ${RAM_PROJECT_FOLDER}/simian_results
    fi
    cp -r $FILES/$i $SRC_SIMIAN_FOLDER/
    for compressed in $SRC_SIMIAN_FOLDER/*
    do
        BASENAME="$(basename $compressed)"
	if [ $2 = "default" ]; then
        java -jar -Xmx1024m /home/cragkhit/Documents/CloneOverflow/tools/simian/bin/simian-2.3.35.jar -threshold=10 "/dev/shm/cragkhit/**/*.java" > "${RAM_PROJECT_FOLDER}"/simian_results/"${BASENAME}".txt
    elif [ $2 = "fse13" ]; then
		java -jar -Xmx1024m /home/cragkhit/Documents/CloneOverflow/tools/simian/bin/simian-2.3.35.jar -threshold=5 -ignoreCurlyBraces+ -ignoreIdentifiers+ -ignoreIdentifierCase+ -ignoreStrings+ -ignoreCharacters+ -ignoreSubtypeNames+ -balanceSquareBrackets+ "/dev/shm/cragkhit/**/*.java" > "${RAM_PROJECT_FOLDER}"/simian_results/"${BASENAME}".txt
	fi
    done
    rm -rf $SRC_SIMIAN_FOLDER
    printf "Done\n"
done
