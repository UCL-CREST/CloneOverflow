import glob2
from subprocess import Popen, PIPE
import os, sys, traceback


file_id_list = []


def get_methods(file):
    p = Popen(["java", "-jar", "MethodExtractor-1.0-SNAPSHOT.jar", file], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    # print output.strip()
    # print err.strip()
    try:
        with open("methods.txt", "r") as f:
            all_methods = f.read()
            methods = all_methods.split("@@==UCL==@@")
        return methods
    except Exception as e:
        print file + ": no method found."

    return []


def get_file_list(home_dir, filter):
    """
    Get all files with the given extension in a folder recursively
    :param home_dir: the location to search for files
    :param filter: filter of the file's extension (e.g. *.java)
    :return: list of files
    """
    all_files = glob2.glob(home_dir + '/**/' + filter)
    return all_files


def createFileId(file):
    global file_id_list
    if file not in file_id_list:
        file_id_list.append(file)
        fileid = file_id_list.index(file)
    else:
        fileid = file_id_list.index(file)
    return fileid


def saveFileId():
    global file_id_list
    # print file_id_list
    try:
        os.remove("fileidmap.txt")
    except Exception as e:
        print "couldn't remove fileidmap.txt file."

    for index, file in enumerate(file_id_list):
        writefile("fileidmap.txt", str(index) + "," + file + "\n", "a", False)

    print "saved fileidmap.txt."


def writefile(filename, fcontent, mode, isprint):
    """
    Write the string content to a file
    copied from
    http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    :param filename: name of the file
    :param fcontent: string content to put into the file
    :param mode: writing mode, 'w' overwrite every time, 'a' append to an existing file
    :return: N/A
    """
    # try:
    file = open(filename, mode)
    file.write(fcontent.encode('ISO-8859-1', 'ignore'))
    file.close()

    if isprint:
        print "saved:" + filename


def main():
    # remove the old output file
    try:
        os.remove("so.txt")
    except Exception as e:
        print "couldn't remove file."
        traceback.print_exc(file=sys.stdout)

    # get list of Java files
    javafiles = get_file_list(sys.argv[1], "*.java");
    # start method extraction
    for jfile in javafiles:
        methods = get_methods(jfile)
        print "Processing: " + jfile + ":", len(methods), "methods."
        for i, method in enumerate(methods):
            writefile("so.txt", "===@@@UCI===\n", "a", False)
            id = createFileId(jfile)
            writefile("so.txt", str(id) + "\n", "a", False)
            writefile("so.txt", str(i) + "\n", "a", False)
            writefile("so.txt", method.strip() + "\n", "a", False)

    saveFileId()


main()
