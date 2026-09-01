# Random Number Generator for Math Practice

import sys
import os
import random
import operator


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def start():

    choices_start = ("Start", "start", "run", "1")
    choices_about = ("About", "about", "abt")
    choices_exit = ("Exit", "exit", "0")

    while True:
        cls()

        print("=== Welcome to the Random Number Generator Program 0/ ===")

        print("\n- Start")
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


def main_menu():

    choices_repeat = ("", "Y", "y")

    while True:

        cls()
        print("=== Random Number Generator ===")
        num1 = random.randrange(1, 20)
        num2 = random.randrange(1, 20)

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
