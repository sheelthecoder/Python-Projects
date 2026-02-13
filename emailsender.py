import smtplib

to = input("Enter the email of recipent:\n")

content = input("Enter the content for the mail\n")

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','1234')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()
    
sendmail(to,content)