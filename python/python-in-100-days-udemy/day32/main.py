import smtplib

myEmail = "m.sadegh.hemati.dev@gmail.com"
myPassword = "rxsf kumx laht cvfh"

try:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=myEmail, password=myPassword)
    msg = "Subject: Test Email\n\nHello, this is a test email."
    connection.sendmail(from_addr=myEmail, to_addrs="memarseti@gmail.com", msg=msg)
    print("Email sent successfully.")
finally:
    connection.close()
