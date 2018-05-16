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


def modify_token_file(file):
    starting_id = 4000000
    fname = file
    with open(fname) as f:
        content = f.readlines()
    for c in content:
        split = c.split('@#@')
        loc = split[0]
        token = split[1]
        locsplit = loc.split(',')
        first = locsplit[0]
        second = locsplit[1]
        # print(first, second)
        new_id = int(second) + starting_id
        write_file(file.replace('.', '-new.'), '-1,' + str(new_id) + '@#@' + token, 'a', False)


def modify_header_file(file):
    starting_id = 4000000
    fname = file
    with open(fname) as f:
        content = f.readlines()
    for c in content:
        split = c.split(',')
        print(split)
        loc = int(split.pop(0))
        pathc = ",".join(split)
        print(loc, pathc)
        write_file(file.replace('.', '-new.'), str(loc + starting_id) + ',' + pathc, 'a', False)


def main():
    modify_token_file('so-license-tokens.file')
    modify_header_file('so-license-headers.file')


main()


