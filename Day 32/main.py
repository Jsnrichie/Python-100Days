##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import pandas
from random import choice

# Email login
my_email = "YOUR EMAIL"
password = "YOUR PASS"

letter_paths = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

#Get todays date
today = dt.datetime.now()
today_day = today.day
today_month = today.month


dataframe = pandas.read_csv("birthdays.csv")
friend_list = dataframe.to_dict(orient="records")
# print(friend_list)

for person in friend_list:
    #Check if today is someone's birthday
    if person["month"] == today_month and person["day"] == today_day:
        print(f"Hey {person['name']}! It's your birthday! ")

        #pick random letter and condense into single string
        letter_choice = choice(letter_paths)
        with open(file=letter_choice, mode="r") as file:
            letter_list = file.readlines()
            letter = "".join(letter_list)

        #send mail
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr= my_email,
                to_addrs= person["email"],
                msg=f"Subject:Happy Birthday!!\n\n{letter.replace('[NAME]', person['name'])}"
            )
