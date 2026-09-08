# Random Number Generator for Math Practice
import sys
import os
import random
import operator


def cls():
    os.system("cls" if os.name == "nt" else "clear")


#Values for the random number generator
#------------------------------------------------------------
min_val_1 = 0
max_val_1 = 10

min_val_2 = 0
max_val_2 = 10

random_number_set_1 = random.randrange(min_val_1, max_val_1)
random_number_set_2 = random.randrange(min_val_2, max_val_2)
#-----------------------------------------------------------
#For the assigned operation
assigned_operation = "+"


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

    global format_selected

    def format():

        global assigned_operation

        while True:

            global addition_choices, subtraction_choices, multiplication_choices

            addition_choices = ("Addition", "Add", "addition", "add", "+")
            subtraction_choices = ("Subtraction", "Subtract", "subtraction", "subtract", "Minus", "minus", "-")
            multiplication_choices = ("Multiplication", "multiplication", "Multiply", "multiply", "*")

            cls()
            print("=== Settings ===")
            print("\nChange format")
            print("Change to which operation?")

            user_input = input(": ")

            assigned_operation = user_input

            if user_input in addition_choices:
                assigned_operation = "+"
                print(f"Operation changed to {assigned_operation}!")
                input(": ")
                start()
            elif user_input in subtraction_choices:
                assigned_operation = "-"
                print(f"Operation changed to {assigned_operation}!")
                input(": ")
                start()
            elif user_input in multiplication_choices:
                print(f"Operation channged to {assigned_operation}!")
                input(": ")
                start()
            else:
                print("\nInvalid! Please select an option.")
                input("\n: ")
    

    def change_int():
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

    format_choices = ("Change Format ", "change format", "Format", "format", "f", "F")
    change_int_choices = ("Change Int Range", "change int", "Int", "int")

    while True:
        cls()
        print("=== Settings ===")
        print("\n- Change format")
        print("- Change Int Range")

        user_input = input("\n: ")

        if user_input in format_choices:
            format()
        elif user_input in change_int_choices:
            change_int()
        elif user_input == "":
            print("\nInvalid! Please select an option.")
            input("\n: ")
        else:
            print("\nInvalid! Please select an option.")
            input("\n: ")



def main_menu():

    global assigned_operation

    choices_repeat = ("", "1", "Y", "y")
    choices_exit = ("N", "n", "0", "Exit", "exit")

    def addition():
        while True:
            global min_val_1, min_val_2, max_val_1, max_val_2, random_number_set_1, random_number_set_2
            global assigned_operation

            choices_repeat = ("", "1", "Y", "y")
            choices_exit = ("N", "n", "0", "Exit", "exit")
            
            cls()
            print("=== Random Number Generator ===")
            num1 = random.randrange(min_val_1, max_val_1)
            num2 = random.randrange(min_val_2, max_val_2)

            #This is the display/generator
            #-------------------
            print("\n", "", num1)
            print(assigned_operation, num2)
            #-------------------

            answer = num1 + num2

            print("\nGenerate another set?")

            user_input = input("\n: ")

            if user_input in choices_repeat:
                addition()
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

    def subtraction():
            while True:
                global min_val_1, min_val_2, max_val_1, max_val_2, random_number_set_1, random_number_set_2
                global assigned_operation
    
                choices_repeat = ("", "1", "Y", "y")
                choices_exit = ("N", "n", "0", "Exit", "exit")
                
                cls()
                print("=== Random Number Generator ===")
                num1 = random.randrange(min_val_1, max_val_1)
                num2 = random.randrange(min_val_2, max_val_2)
    
                #This is the display/generator
                #-------------------
                print("\n", "", num1)
                print("-", num2)
                #-------------------
    
                answer = num1 - num2
    
                print("\nGenerate another set?")
    
                user_input = input("\n: ")
    
                if user_input in choices_repeat:
                    subtraction()
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

    def multiplication():
            while True:
                global min_val_1, min_val_2, max_val_1, max_val_2, random_number_set_1, random_number_set_2
                global assigned_operation
    
                choices_repeat = ("", "1", "Y", "y")
                choices_exit = ("N", "n", "0", "Exit", "exit")
                
                cls()
                print("=== Random Number Generator ===")
                num1 = random.randrange(min_val_1, max_val_1)
                num2 = random.randrange(min_val_2, max_val_2)
    
                #This is the display/generator
                #-------------------
                print("\n", "", num1)
                print("*", num2)
                #-------------------
    
                answer = num1 * num2
    
                print("\nGenerate another set?")
    
                user_input = input("\n: ")
    
                if user_input in choices_repeat:
                    multiplication()
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

    def division():
        while True:
            global min_val_1, min_val_2, max_val_1, max_val_2, random_number_set_1, random_number_set_2
            global assigned_operation
        
            choices_repeat = ("", "1", "Y", "y")
            choices_exit = ("N", "n", "0", "Exit", "exit")
                    
            cls()
            print("=== Random Number Generator ===")

            num1 = random.randrange(min_val_1, max_val_1)
            num2 = random.randrange(min_val_2, max_val_2)
        
            #This is the display/generator for Division format (Long Division)
            #-------------------
            print("   ________")
            print(num1,"|",num2)
            #-------------------

            try:
                answer = num1 / num2
            except ZeroDivisionError:
                print("\nZero Division Error!")
                print("Syntax Error.")

            print("\nGenerate another set?")
        
            user_input = input("\n: ")
        
            if user_input in choices_repeat:
                division()
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

    def main_menu_screen():

        global assigned_operation, addition_choices, subtraction_choices, multiplication_choices, add_subtract_multiply_choices

        addition_choices = ("Addition", "Add", "addition", "add", "+")
        subtraction_choices = ("Subtraction", "Subtract", "subtraction", "subtract", "Minus", "minus", "-")
        multiplication_choices = ("Multiplication", "multiplication", "Multiply", "multiply", "*")
        division_choices = ("Division", "division", "Divide", "divide", "/")

        choices_back = ("Back", "back", "0")

        while True:
            cls()
            print("=== Random Number Generator ===")

            print("\n- Addition")
            print("- Subtraction")
            print("- Multiplication")
            print("- Division")
            print("- Back")

            user_input = input("\n: ")

            if user_input in addition_choices:
                addition()
            elif user_input in subtraction_choices:
                subtraction()
            elif user_input in multiplication_choices:
                multiplication()
            elif user_input in division_choices:
                division()
            elif user_input in choices_back:
                start()
            else:
                print("Invalid! Please select an option.")
                input("\n: ")

    main_menu_screen()

        


start()
