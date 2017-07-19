import urllib2
import sys, traceback
import json
import re


def writefile(filename, fcontent, mode):
    """
    Write the string content to a file
    copied from
    http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    :param filename: name of the file
    :param fcontent: string content to put into the file
    :param mode: writing mode, 'w' overwrite every time, 'a' append to an existing file
    :return: N/A
    """
    try:
        file = open(filename, mode)
        file.write(fcontent.encode('utf-8', 'ignore'))
        file.close()
    except Exception as e:
        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60


reload(sys)
sys.setdefaultencoding("ISO-8859-1")

for pageno in range(1,50):

    print_buffer = ''
    print 'page' + str(pageno) + ','
    print_buffer += 'page' + str(pageno) + ',' + '\n'

    response = urllib2.urlopen('https://stackoverflow.com/users?page=' + str(pageno) + '&tab=reputation&filter=all')
    html = response.read()
    lines = html.split('\n')


    for index, line in enumerate(lines):

        if '<a href="/users/' in line and '<div class=\"gravatar' in line:

            parts = line.split('"')
            response2 = urllib2.urlopen('https://stackoverflow.com/' + parts[1])
            html2 = response2.read()
            # print html2
            lines2 = html2.split('\n')

            for index, line2 in enumerate(lines2):

                # Here re.findall() returns a list of all the found email strings
                # emails = re.findall(r'[\w\.-]+@[\w\.-]+', line2)
                #
                # for email in emails:
                #     # do something with each found email string
                #     print email

                if 'email' in line2.lower() or 'e-mail' in line2.lower():

                    # found email on Stack Overflow profile!
                    print parts[1] + ',' + 'https://stackoverflow.com/' + parts[1] + ',' + line2
                    print_buffer += parts[1] + ',' + '=HYPERLINK("https://stackoverflow.com/' + parts[1] + '"),' + line2 + '\n'

                    break
                else:
                    # go to GitHub (if any)
                    if '<a href="https://github.com' in line2:

                        email = None
                        github_url = line2.split('"')[1]

                        # github_url = line2.split('"')[1].replace('github.com', 'api.github.com/users')
                        # print line2.split('"')[1]
                        # responsex = urllib2.urlopen(line2.split('"')[1])
                        # writefile(str(index) + ".txt", responsex.read().encode('utf-8'), 'w')
                        #
                        # print github_url

                        # try:
                        #     # try to go to GitHub and grab emails from there
                        #     response3 = urllib2.urlopen(github_url)
                        #     json_response = response3.read()
                        #     json_data = json.loads(json_response)
                        #     print json_data['email']
                        #     # email = json_data['email']
                        # except ValueError as e:
                        #     print "ERROR: not github url."
                        # except urllib2.HTTPError as he:
                        #     print "ERROR: exceeded github rate limit."
                        #
                        # if email is None:
                        #     print parts[1] + ',' + github_url + ','
                        #     print_buffer += parts[1] + ',' + github_url + ',\n'
                        # else:
                        #     print parts[1] + ',' + github_url + ',' + email
                        #     print_buffer += parts[1] + ',' + github_url + ',' + email + '\n'

                        if 'https://github.com/' in github_url:
                            print parts[1] + ',' + github_url + ','
                            print_buffer += parts[1] + ',' + '=HYPERLINK("' + github_url + '"),\n'

    writefile('emails.csv', print_buffer, 'a')