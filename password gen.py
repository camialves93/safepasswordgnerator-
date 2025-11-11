import random
import string

def password_generator(Length_pass=8): 
    # Define os caracteres possíveis para a senha
    ascii_options = string.ascii_letters
    number_options = string.digits
    punct_options = string.punctuation
    options = ascii_options + number_options + punct_options

    # Gera a senha aleatória sem usar join
    password_user = ""
    for _ in range(Length_pass):
        password_user += random.choice(options)
    return password_user

print("The NIST standard recommends passwords with at least 8 characters.")
follow_standard = input("Do you want to follow the NIST standard? (yes or no): ").strip().lower()

if follow_standard == "yes":
    user_choice = 8
else:
    user_choice = input("How many characters in your password? (minimum 8): ").strip()
    if user_choice.isdigit():
        user_choice = int(user_choice)
    else:
        print("Invalid entry! Please enter a number.")
        quit()

    if user_choice < 8:
        print("Password length must be at least 8 characters according to security best practices.")
        quit()

# Gera e exibe a senha
respon = password_generator(Length_pass=user_choice)
print(f"\nPassword generated ({user_choice} characters):\n{respon}")
