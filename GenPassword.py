import random
from random import randint

import pyperclip


def get_letters():

    # Creates an array for the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']

    # Randomly selects a letter from alphabet
    select_letter = random.choice(alphabet)

    letter = select_letter
    #Randomly capitalizes the letter; 0 = false, 1 = true
    capitalize_letter = randint(0, 1)
    if(capitalize_letter == 1):
        letter = letter.capitalize()
        return letter

    else:

        return letter


    return capitalize_letter

# Randomly gets a number between 0 - 9
def get_numbers():
    number = randint(0, 9)
    number = str(number)
    return number

def get_alphanum():

    select_random = randint(0, 1)
    
    if(select_random == 1):
        return get_letters()
    else:
        return get_numbers()



def get_spcl_char():
    character = ['!', '@', '#', '$', '%', '&', '(', ')', '+', '*', '-', '_',
                 '.', '?', '[', ']', ]
    select_char = random.choice(character)
    
    return select_char


def get_all_char():
# Created to make it more random
    select_random = randint(0, 2)
    
    if(select_random == 1):
        return get_letters()

    elif(select_random == 0):
        return get_spcl_char()

    else:
        return get_numbers()



def generate_password():
    password = []
    yes = ['yes', 'YES', 'y']

    try:
        pw_length_input = int(input("Password Length: "))
        spcl_char = input("Do you want special Characters? ")

# Calls functions depending how what the user inputs in pw_length
        for _ in range(pw_length_input):
            select_random = randint(0, 1)

            if(select_random == 0):
                password.append(get_alphanum())

            else:
                select_random = randint(0, 1)
                if(select_random == 0):

                    if(spcl_char in yes):
                        password.append(get_all_char())
                        
                    else:
# Line inputed to add more variety and lessen the psuedo random
                        password.append(get_alphanum())
                else:
                    password.append(get_all_char())


    except ValueError:
        print("Please enter a number!")
        generate_password()
        
    password = ''.join(password)
    print(password)
    print(len(password))

# This copies the password to the clipboard for the user to paste where they please    
    pyperclip.copy(password)

# TODO:
# Save past generated passwords, up to 10+
# Separate x amount of letters with '-' or '.'
# Encrypt past passwords
# Clean up code.
    
generate_password()