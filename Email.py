import smtplib

#Senders Info!
Email =  "hotbrewmills@gmail.com"
Pass = "ckdgrquvbmaohfhb"
Name = input("Enter Your Name: ")

sent_from = Email

RecEmail = input("Send Email to: ")
Subject = input("Subject: ")
Message = input("Message: ")
sent_to = RecEmail

email_text = """\

From: %s

To: %s

Subject: %s


%s

""" % (sent_from, ", ".join(sent_to), Subject, Message)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(Email, Pass)
    smtp_server.sendmail(Email, RecEmail, Message)
    smtp_server.close()
    print("Email sent Successfully!")
except Exception as ex :
    print("Failed!", ex)
