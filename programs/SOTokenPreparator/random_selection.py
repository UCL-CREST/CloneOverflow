import random


def write_file(filename, fcontent, mode, isprint):
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


def random_select(file, amount):
    random.seed(13)
    with open(file) as f:
        clones = f.readlines()
    for i in range(0, amount):
        # print(i, random.choice(clones), end='')
        write_file('license-github-random.csv', random.choice(clones), 'a', False)


def main():
    write_file('license-github-random.csv', 'github,ghstart,ghend,so,sostart,soend,solicense,ghlicense\n', 'a', False)
    random_select(
        '/Users/Chaiyong/Documents/phd/2017/CloneOverflow/experiment/results/license-github/combined.csv',
        400)


main()
