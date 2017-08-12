FILES=/scratch0/NOT_BACKED_UP/crest/gbianco/QualitasCorpus-20130901r/projects
RAM_PROJECT_FOLDER=/dev/shm/cragkhit
SRC_NICAD_FOLDER=/dev/shm/cragkhit/src

while read i; do    
    printf "*** Processing: $FILES/$i ***\n"
    if [ ! -d $SRC_NICAD_FOLDER ]; then
        mkdir $SRC_NICAD_FOLDER
    fi
    cp -r $FILES/$i $SRC_NICAD_FOLDER/
    for compressed in $SRC_NICAD_FOLDER/*
    do
        BASENAME="$(basename $compressed)"
        java -jar /scratch0/NOT_BACKED_UP/crest/gbianco/tools/iclones-0.2/jar/iclones.jar -minblock 10 -minclone 50 -input "/dev/shm/cragkhit" > "${RAM_PROJECT_FOLDER}"/iclones_results/"${BASENAME}".txt
    done
    rm -rf $SRC_NICAD_FOLDER
    printf "Done\n"
done <$1
