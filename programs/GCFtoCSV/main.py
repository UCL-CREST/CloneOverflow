import xml.etree.ElementTree
import sys



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
        print("saved:" + filename)


def main():
    scc_clones = xml.etree.ElementTree.parse(sys.argv[1])
    clones = scc_clones.findall('CloneClass')
    output = ''
    num_pairs = len(clones)
    for idx, clone in enumerate(clones):
        pair = clone.findall('Clone')
        output += pair[0][0][0].text + ',' + pair[0][0][1].text + ',' + pair[0][0][2].text + ','
        output += pair[1][0][0].text + ',' + pair[1][0][1].text + ',' + pair[1][0][2].text + '\n'

    print('processed:', num_pairs + 1, 'files')
    writefile(sys.argv[1].replace('.xml', '.csv'), output, 'w', True)

main()
