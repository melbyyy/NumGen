# Random Number Generator for Math Practice

import sys
import os
import random
import operator


def cls():
    os.system("cls" if os.name == "nt" else "clear")


min_val_1 = 0
max_val_1 = 10

min_val_2 = 0
max_val_2 = 10

random_number_set_1 = random.randrange(min_val_1, max_val_1)
random_number_set_2 = random.randrange(min_val_2, max_val_2)


def start():

    choices_start = ("Start", "start", "run", "1")
    choices_settings = ("Settings", "settings", "s", "Change", "change")
    choices_about = ("About", "about", "abt")
    choices_exit = ("Exit", "exit", "0")

    while True:
        cls()

        print("=== Welcome to the Random Number Generator Program 0/ ===")

        print("\n-----------------------------")
        print("v 1.1 Beta")
        print("              .               ")
        print("            +@@@#             ")
        print("            +@@@#             ")
        print("            +@@@#             ")
        print("     :*#####%@@@@#####*-      ")
        print("    :@@@@@@@@@@@@@@@@@@@=     ")
        print("     .******%@@@%******:      ")
        print("            +@@@#             ")
        print("            +@@@#             ")
        print("            +@@@#             ")
        print("              .               ")
        print("\n-----------------------------")

        print("\n- Start")
        print("- Settings")
        print("- About")
        print("- Exit")

        user_input = input("\n: ")

        if user_input in choices_start:
            cls()
            print("Starting...")
            print("Press enter to continue.")
            input("\n: ")
            main_menu()
        elif user_input in choices_about:

            # About Page!
            cls()
            print("=== About ===")
            print("\nHello! This program was made for the purpose of making practicing Math Fundamentals a bit easier for students!")
            print("As of now this is a current demo so not all features are added yet! There will be more updates to come!")
            input("\n: ")
        elif user_input in choices_settings:
            settings()
        elif user_input in choices_exit:
            cls()
            print("Thank you for using this program. 0/")
            input("\n: ")
            cls()
            sys.exit()
        elif user_input == "":
            print("\nInvalid! Please select an option.")
            input("\n: ")
        else:
            print("\nInvalid! Please select an option.")
            input("\n: ")

# Settings to change randrange


def settings():

    global min_val_1, min_val_2, max_val_1, max_val_2, random_number_set

    while True:
        cls()
        print("=== Settings ===")

        print("\nChange Int Range:")
        print("\n")
        print("Enter Minimum Number")

        try:
            min_val_1 = int(input(": "))
            min_val_2 = min_val_1
            break
        except ValueError:
            print("Please enter a number.")
            input(": ")

    while True:
        cls()
        print("=== Settings ===")

        print("\nChange Int Range:")
        print("\n")
        print("Enter Maximum Number")

        try:
            max_val_1 = int(input(": "))
            max_val_2 = max_val_1
            break
        except ValueError:
            print("Please enter a number.")
            input(": ")

    while True:
        print(f"Your range_1 is: {min_val_1} and {max_val_1}")
        print(f"Your range_2 is: {min_val_2} and {max_val_2}")
        input(": ")
        start()


def main_menu():

    global min_val_1, min_val_2, max_val_1, max_val_2, random_number_set_1, random_number_set_2

    choices_repeat = ("", "1", "Y", "y")
    choices_exit = ("N", "n", "0", "Exit", "exit")

    while True:

        cls()
        print("=== Random Number Generator ===")
        num1 = random.randrange(min_val_1, max_val_1)
        num2 = random.randrange(min_val_2, max_val_2)

        print("\n", "", num1)
        print("+", num2)

        answer = num1 + num2

        print("\nGenerate another set?")

        user_input = input("\n: ")

        if user_input in choices_repeat:
            main_menu()
        elif user_input in choices_exit:
            start()
        elif user_input == "show":
            print(answer)
            input(": ")
        elif user_input == answer:
            print("Correct!")
            input(": ")
        else:
            cls()
            print("Invalid! Please select an option.")
            input("\n: ")


start()
