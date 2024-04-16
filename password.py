import string
import random

def generate_password(min_length, numbers=True, special_characters=True):
    a1 = string.ascii_letters
    a2 = string.digits
    a3 = string.punctuation
    
    characters = a1
    if numbers:
        characters += a2
    if special_characters:
        characters += a3
        
    pwd =""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in a2:
            has_number = True
        elif new_char in a3:
            has_special = True
            
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
            
    return pwd
min_length = int(input("Enter password length: "))
has_number = input("Do you want numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("Your password is: ", pwd)