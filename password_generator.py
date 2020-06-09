#!/usr/bin/python3.6
import os
import random
import time
# This script give help to you fot create passwords
# To use this, just only need enter a password length
# then wait for script output
# You can specific a file for passwords
# If not the program can save all passwords generated in single text file


# CREATE FILE - GET FILE PATH FOR SAVE PASSWORDS
# Get absolute path for file called 'passwords'
def get_file_dict():
    os.chdir("~/Escritorio")
    file_path = ""  # absolute file path
    # file exists or not
    if os.path.exists("passwords"):
        file_path = os.getcwd() + "/" + "passwords"  # set path
        # print some file path info to user
        print("File found in: {}".format(os.getcwd() + "/" + "passwords"))
    # create file if this not exists
    else:
        create_file()  # create file
        get_file_dict()  # recall this function

    return file_path  # return the file path


# Create an empty file to storage all generated passwords
# The path for are decided by system not by user
# The file are created in Desktop user folder
def create_file():
    # change work directory to default directory
    os.chdir("~/Escritorio")
    # create file
    with open("passwords", "w") as file:
        file.writelines("# File generate in {}.\n".format(time.ctime()))
        # print absolute file path
        print("  File created in: {}".format(os.getcwd()))


password = ""


def generate_password(dic_password_options):
    password_length = dic_password_options["length"]
    password_chars = dic_password_options["chars"]
    global password
    password = ""
    for i in range(0, password_length):
        password += password_chars[random.randint(0, len(password_chars)-1)]


def get_password_info():
    print("\x1bc")  # clear screen output
    password_options = {}
    while True:
        # show user options
        print("  Select length type: ")
        print("    1. Auto (System)")
        print("    2. Len (User)")
        user_option = input("    -> Enter your option: ")

        # select option was correct
        # system decide length for password
        if user_option == "1":
            print("  Password length decided by system")
            password_options["length"] = random.randint(8, 14)  # This number means that system decided the length
            break
        # user must write length for password
        elif user_option == "2":
            while True:
                # get user input
                password_length = input("\n    -> Enter length for password: ")
                # user input is a digit value or not
                if password_length.isdigit():
                    # value are great than 2
                    if int(password_length) > 2:
                        print("  correct...")
                        password_options["length"] = int(password_length)
                        break  # exit
                    # value must be great than 2
                    else:
                        print("  password length must be great than 2")
                        print("  Try again...")
                # value must be a digit
                else:
                    print("  password length must be a number.")
                    print("  Try again...")
            break
        # option select by user no are correct or not exists
        else:
            print("  the option '{}' not is valid.".format(user_option))
            print("  Try again...")

    # get characters that can be included in password
    while True:
        print("\n  Select characters to include in password: ")
        print("    1. Numbers, Letters (uppercase and lowercase)")
        print("    2. Numbers, All Letters and Symbols")
        print("    3. Only numbers")
        print("    4. Only letters (uppercase and lowercase")
        user_option = input("    -> Option: ")
        if user_option == "1":
            password_options["chars"] = get_characters(1)
            break
        elif user_option == "2":
            password_options["chars"] = get_characters(2)
            break
        elif user_option == "3":
            password_options["chars"] = get_characters(3)
            break
        elif user_option == "4":
            password_options["chars"] = get_characters(4)
            break
        else:
            print("  the option '{}' not is valid".format(user_option))
            print("  Try again...")

    return password_options


# This function return a string with valid characters to make password
# int_filter specific that characters can be included in password
# int_filter = 1: Numbers, Letters Mm
# int_filter = 2: Numbers, Letters Mm and Symbols as (*.,-_+=?¡¿!#$%&;)
# int_filter = 3: Only Numbers
# int_filter = 4: Only Letters Mm
def get_characters(int_filter):
    letters_lowercase = "abcdefghijklmnopqrstuvwxyz"
    letter_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_all = "1234567890"
    valid_symbols = "!#$%&=?'¡¿-_.;,"

    # password can include only numbers and letters Mm
    if int_filter == 1:
        build_string = letter_uppercase + numbers_all + letters_lowercase
    # password can include all valid chars
    elif int_filter == 2:
        build_string = numbers_all + letters_lowercase + valid_symbols + letter_uppercase
    # password can only include numbers
    elif int_filter == 3:
        build_string = numbers_all
    # password can only include letters Mm
    else:
        build_string = letter_uppercase + letters_lowercase

    # return builder string
    return build_string


generate_password(get_password_info())
time.sleep(0.1)
print("  Your password is: {}".format(password))
option = input("\n  Do you want save password [Y]yes, [N]no:")
