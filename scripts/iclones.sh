FILES=/scratch0/NOT_BACKED_UP/crest/gbianco/QualitasCorpus-20130901r/projects
RAM_PROJECT_FOLDER=/dev/shm/cragkhit
SRC_ICLONES_FOLDER=/dev/shm/cragkhit/src

while read i; do    
    printf "*** Processing: $FILES/$i ***\n"
    if [ ! -d $SRC_ICLONES_FOLDER ]; then
        mkdir $SRC_ICLONES_FOLDER
    fi
    cp -r $FILES/$i $SRC_ICLONES_FOLDER/
    for compressed in $SRC_ICLONES_FOLDER/*
    do
        BASENAME="$(basename $compressed)"
        java -jar /scratch0/NOT_BACKED_UP/crest/gbianco/tools/iclones-0.2/jar/iclones.jar -minblock 10 -minclone 50 -input "/dev/shm/cragkhit" > "${RAM_PROJECT_FOLDER}"/iclones_results/"${BASENAME}".txt
    done
    rm -rf $SRC_ICLONES_FOLDER
    printf "Done\n"
done <$1
