#This project was developed for educational and portfolio purposes to demonstrate my programming skills and technical understanding.

import random
import string

def password_generator(Length_pass=8): 
    ascii_options = string.ascii_letters
    number_options = string.digits
    punct_options = string.punctuation
    options = ascii_options + number_options + punct_options

    password_user = ""
    for _ in range(Length_pass):
        password_user = password_user + random.choice(options)

    return password_user


user_choice = input("How many characters in the password?\nThe password length is 8 characters or more : ")

if user_choice.isdigit():
    user_choice = int(user_choice)
else: 
    print("Password length must be greater than zero.")
    quit()

if user_choice < 8:
    print("Password length must be at least 8 characters!")
    quit()

respon = password_generator(Length_pass=user_choice)
print(f"Password generated:\n{respon}")
