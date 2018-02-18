import subprocess as sp
import os


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
    file.write(fcontent)
    file.close()

    if isprint:
        print "saved:" + filename


with open("log.txt", "r") as f:
    all_snippets = f.read().split("\n")
    for snippet in all_snippets:
        with open("/Users/Chaiyong/Downloads/stackoverflow/" + snippet, "r") as sofile:
            tmp = sp.call('clear', shell=True)
            print snippet
            code = sofile.read()
            print "----------"
            print code
            print "----------"
            selection = raw_input("Should I move it? (y/n)")
            if selection.lower() == "y":
                print "Moving: " + "/Users/Chaiyong/Downloads/stackoverflow/" + snippet + " to " + \
                      "/Users/Chaiyong/Downloads/stackoverflow/filtered_so_snippets/pmdcpd/"\
                      + snippet.replace("stackoverflow_formatted/","")
                writefile("/Users/Chaiyong/Downloads/stackoverflow/filtered_so_snippets/pmdcpd/movedfiles.txt",
                          "/Users/Chaiyong/Downloads/stackoverflow/" + snippet + "," + \
                      "/Users/Chaiyong/Downloads/stackoverflow/filtered_so_snippets/pmdcpd/"\
                      + snippet.replace("stackoverflow_formatted/",""), "a", False)
                os.rename("/Users/Chaiyong/Downloads/stackoverflow/" + snippet,
                          "/Users/Chaiyong/Downloads/stackoverflow/filtered_so_snippets/pmdcpd/"
                          + snippet.replace("stackoverflow_formatted/",""))

