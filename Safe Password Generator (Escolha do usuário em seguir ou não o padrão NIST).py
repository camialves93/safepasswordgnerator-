#This project was developed for educational and portfolio purposes to demonstrate my programming skills and technical understanding.

import random
import string

def password_generator(Length_pass=8): 
    ascii_options = string.ascii_letters
    number_options = string.digits
    punct_options = string.punctuation
    options = ascii_options + number_options + punct_options


    password_user = ''.join(random.choice(options) for _ in range(Length_pass))
    return password_user

print("The NIST standard recommends passwords with at least 8 characters.")
follow_standard = input("Do you want to follow the NIST standard? (yes or no): ").strip().lower()

if follow_standard == "yes":
    
    while True:
        try:
            user_choice = int(input("Choose the password length (8 to 15 characters): "))
            if 8 <= user_choice <= 15:
                break
            else:
                print("Password length must be between 8 and 15 characters.")
        except ValueError:
            print("Invalid entry!.")
else:
   
    while True:
        try:
            user_choice = int(input("Enter password length: "))
            if user_choice > 0:
                break
            else:
                print("Password length must be greater than zero.")
        except ValueError:
            print("Invalid entry! Please enter a number.")


respon = password_generator(Length_pass=user_choice)
print(f"\nPassword generated ({user_choice} characters):\n{respon}")
