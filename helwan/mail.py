
import smtplib


def sendmail(mail , msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("helwaneng558@gmail.com", "amrezzat")
    message = 'Subject: {}\n\n{}'.format("Department confirmation", msg)
    server.sendmail("helwaneng558@gmail.com", mail, message)
    server.quit()