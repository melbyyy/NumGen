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

    def help():
        #These are the list of commands for starting page!

        global choices_start, choices_settings, choices_about, choices_help, choices_exit

        while True:
            cls()
            print("=== Help ===")
            print("\nHere are the sets of commands for this page!")

            print("\n[ Start ]")
            print()
            print(*choices_start, sep = '|')
            print("\n")

            print("[ Settings ]")
            print()
            print(*choices_settings, sep = '|')
            print("\n")

            print("[ About ]")
            print()
            print(*choices_about, sep = '|')
            print("\n")

            print("[ Help ]")
            print()
            print(*choices_help, sep = '|')
            print("\n")

            print("[ Exit ]")
            print()
            print(*choices_exit, sep = '|')
            input("\n: ")

            start()

    global choices_start, choices_settings, choices_about, choices_help, choices_exit

    choices_start = ("Start", "start", "run", "1")
    choices_settings = ("Settings", "settings", "s", "Change", "change")
    choices_about = ("About", "about", "abt")
    choices_help = ("Help", "help","HELP" "?")
    choices_exit = ("Exit", "exit", "0")

    while True:
        cls()

        print("=== NumGen < + - / * > ===")

        print("\n-----------------------------")
        print("v 1.2.5 Beta")
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


        start_choices = ("Start", "Settings", "About", "Help", "Exit")

        print()

        for choice in start_choices:
            print('-', choice)

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
        elif user_input in choices_help:
            help()
        elif user_input in choices_exit:
            cls()
            print("Thank you for using this program. 0/")
            input("\n: ")
            cls()
            sys.exit()
        elif user_input == "":
            print("\nInvalid! Please select an option.")
            input("\n")
        else:
            print("\nInvalid! Please select an option.")
            input("\n")

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
            input("\n")
        else:
            print("\nInvalid! Please select an option.")
            input("\n")

        
def main_menu():


#MASS NUMBER GENERATOR SECTION
    def Number_Genetator():

        global choices_back

    #Note to self: This can be optimized!
    #------------------------------------   
        one_digit_values = tuple(random.randrange(10) for value in range(5))
        two_digit_values = tuple(random.randrange(10, 100) for value in range(5))
        three_digit_values = tuple(random.randrange(100, 1000) for value in range(5))
        four_digit_values = tuple(random.randrange(1000, 10000) for value in range(5))
        five_digit_values = tuple(random.randrange(10000, 1000000) for value in range(5))
    #------------------------------------
        
    #------------------------------------
        choices_repeat = ("", "Y", "y")
        choices_back = ('0', 'Back', 'back', 'B', 'b')
    #------------------------------------

        while True:
            cls()

            print('=== Number Generator ===')

            print()

            print('One Digit')
            print(one_digit_values)
            
            print('\nTwo Digits')
            print(two_digit_values)

            print('\nThree Digits')
            print(three_digit_values)

            print('\nFour Digits')
            print(four_digit_values)

            print('\nFive Digits')
            print(five_digit_values)

            user_input = input("\n: ")

            if user_input in choices_repeat:
                Number_Genetator()
            elif user_input in choices_back:
                Num_Gen_Modes()
            else:
                print("\nInvalid! Please select an option.")
                input("\n")



#---------------------------------------  

# OPERATIONS GENERATOR SECTION

# Formats!
# These are the functions for the different operation format and the operation generator!

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
                input("\n")

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
                    input("\n")

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
                    input("\n")

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
                input("\n")
  
    def Number_Generator_in_Operation_Format():

        def help():
            #These are the list of commands for starting page!
        
            global addition_choices, subtraction_choices, multiplication_choices, division_choices
        
            while True:
                cls()
                print("=== Help ===")
                print("\nHere are the sets of commands for this page!")
        
                print("\n[ Addition ]")
                print()
                print(*addition_choices, sep = '|')
                print("\n")
        
                print("[ Subtraction ]")
                print()
                print(*subtraction_choices, sep = '|')
                print("\n")
        
                print("[ Multiplication ]")
                print()
                print(*multiplication_choices, sep = '|')
                print("\n")
        
                print("[ Division ]")
                print()
                print(*division_choices, sep = '|')
                print("\n")
        
                input("\n: ")
        
                Number_Generator_in_Operation_Format()

        global addition_choices, subtraction_choices, multiplication_choices, division_choices
        global choices_help
        
        addition_choices = ("Addition", "Add", "addition", "add", "+")
        subtraction_choices = ("Subtraction", "Subtract", "subtraction", "subtract", "Minus", "minus", "-")
        multiplication_choices = ("Multiplication", "multiplication", "Multiply", "multiply", "*")
        division_choices = ("Division", "division", "Divide", "divide", "/")
        
                
        choices_back = ('0', 'Back', 'back', 'B', 'b')
        
        options_bank = ('Addition', 'Subtraction', 'Multiplication', 'Division')

        while True:
            cls()
            print("=== Random Number Generator ===")

            print("\n------------------")

            for choice in options_bank:
                print('\n-', choice)

            print("\n------------------")

            print()
            print("- Help")
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
            elif user_input in choices_help:
                help()
            elif user_input in choices_back:
                Num_Gen_Modes()
            else:
                print("Invalid! Please select an option.")
                input("\n")

#---------------------------------------  

    def Num_Gen_Modes():

        def help():
            #These are the list of commands for starting page!
                
            global number_generator_choices, operations_generator_choices, choices_help, choices_back
                
            while True:
                cls()
                print("=== Help ===")
                print("\nHere are the sets of commands for this page!")
                
                print("\n[ Number Generator ]")
                print()
                print(*number_generator_choices, sep = '|')
                print("\n")
                
                print("[ Operations Generator ]")
                print()
                print(*operations_generator_choices, sep = '|')
                print("\n")
                
                print("[ Help ]")
                print()
                print(*choices_help, sep = '|')
                print("\n")
                
                print("[ Back ]")
                print()
                print(*choices_back, sep = '|')
                print("\n")
                
                input("\n: ")

                Num_Gen_Modes()

        global number_generator_choices, operations_generator_choices, choices_help, choices_back

        numgen_modes = ("Number Generator", "Operations Generator")


        number_generator_choices = ('1', 'NumGen', 'numgen', 'gen', 'num')
        operations_generator_choices = ('2', 'operation', 'operations' 'op', 'ops')
        choices_help = ("Help", "help","HELP", "?")
        choices_back = ('0', 'Back', 'back', 'B', 'b')

        while True:
            cls()
            print("=== NumGen Main Menu ===")

            print()
            print('[ NumGen Modes ]')
            print()

            print('-------------------')
            for option in numgen_modes:
                print('-', option)
            print('-------------------')

            print('\n- Help')
            print('- Back')

            user_input = input("\n: ")

            if user_input in number_generator_choices:
                Number_Genetator()
            elif user_input in operations_generator_choices:
                Number_Generator_in_Operation_Format()
            elif user_input in choices_help:
                help()
            elif user_input in choices_back:
                start()
            else:
                print("\nInvalid! Please select an option.")
                input("\n")

    Num_Gen_Modes()



            
            




        
start()