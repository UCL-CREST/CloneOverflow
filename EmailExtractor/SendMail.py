import MailController #https://gitlab.cs.ucl.ac.uk/snippets/1
import random
import time
import csv
import traceback
import sys


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
        file.write(fcontent)
        file.close()
    except Exception as e:
        traceback.print_exc(file=sys.stdout)


def read_csv(file):
    """
    Read csv file for email addresses
    :param file: a csv file
    :return: list of email addresses
    """
    recipients = []
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:
            # skip the page header
            if len(row) >= 3:
                # only keep unique emails
                if not row[0].startswith('page') \
                        and row[2] not in recipients\
                        and 'users.noreply.github.com' not in row[2]:
                    recipients.append(row[2])

    return recipients


def main():

    batch_no = 9
    recipients = read_csv('emails' + batch_no + '.csv')
    writefile('email_errors.txt', 'Batch: ' + str(batch_no) + '... sending emails to ' + str(len(recipients)) + ' developers.', 'a')
    # print recipients

    for recipient in recipients:
        try:
            MailController.sendMail(recipient)
            time.sleep(random.randint(1, 3))
        except Exception as e:
            error_msg = time.strftime("%H:%M:%S") + ": " + recipient + ": " + str(e) + "\n"
            writefile('email_errors.txt', error_msg, 'a')

        print('Sent to :' + recipient)


main()