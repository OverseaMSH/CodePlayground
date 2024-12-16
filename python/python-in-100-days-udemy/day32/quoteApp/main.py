import smtplib
import datetime as dt
import random
now = dt.datetime.now()
weekDay = now.weekday()
myEmail = "m.sadegh.hemati.dev@gmail.com"
myPassword = "rxsf kumx laht cvfh"
if weekDay == 0: 
    with open("python/python-in-100-days-udemy/day32/quoteApp/quotes.txt") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        try:
            connection.starttls()
            connection.login(user=myEmail, password=myPassword)
            connection.sendmail(from_addr=myEmail,
                                to_addrs="memarseti@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")
            print("Email sent successfully.")
        finally:
            connection.close()
