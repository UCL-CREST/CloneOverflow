import smtplib
import getpass
from email.mime.text import MIMEText

mailTitle = "Outdated and license-violating code snippets on Stack Overflow" # Mail title

me= 'ucabagk@ucl.ac.uk' # Change with your UCL email address with alias
uclAccount = ""
password = ""


def init():
    global uclAccount
    global password
    uclAccount = raw_input("Enter your ucl email id (not alias): ")
    password = getpass.getpass("Please enter your password: ")


def sendMail(recipient):
    global uclAccount
    global password
    if (uclAccount == ""):
        init()

    mailContent = '''
Dear Developer, 

Since you are one of the top answerers on Stack Overflow, we hope you can help us with a not-for-profit study.

We are researchers in the Software Systems Engineering Group at University College London, UK. We are studying problems caused by outdated and license-violating code snippets on Stack Overflow. 

We have designed a survey to understand these problems and would be grateful if you would complete it:

https://docs.google.com/forms/d/e/1FAIpQLSfagOcgFYYqt0vMLZOoacGQ55SeZyhF1g5MTinTBoD23FRktQ/viewform?usp=sf_link

The survey is completely anonymous and has 11 questions and should only take about 3-5 minutes to complete. 

The survey results will be used only for academic research purposes and we plan to release the results to Stack Overflow and in the form of academic papers and presentations.

Your email address has been extracted from Stack Overflow and GitHub websites and it will not be saved or distributed to other parties.

This research project has been approved by the designated ethics officer in the Computer Science Department at UCL.

Thank you,
Chaiyong Ragkhitwetsagul, Jens Krinke
CREST, Dept. of Computer Science
University College London
www.cs.ucl.ac.uk/staff/C.Ragkhitwetsagul
    '''
    MSG_TEMPLATE="\r\n".join([
        "From: %s"%me,
        "To: %s"%recipient,
        "Subject: %s"%mailTitle,
        "",
        mailContent])

    msg = MSG_TEMPLATE
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(str(uclAccount), str(password))
    server.sendmail(me, recipient, msg)
    server.quit()

