# # Instructions for making a sandwich – write a hierarchy chart for the steps
# # needed to make a sandwich. Then write the Python program to display the
# # steps. (See acme dryer example)
# # 1. First draw the hierarchy of the functions, The main function should:
# # a. Display an intro message to the user (Ex.– “Hello this is how you make a
# # sandwich”)
# # b. Call the step1 function
# # c. Call the step2 function
# # d. Call all remaining step functions
# # e. Display an exit message on a new line (Ex. – “Goodbye”)
# # 2. Step1 function should display step1
# # 3. Step2 function should display step2 … etc.
# # 4. Then write the Python Program
# # 5. Turn in your program to the practice assignment link in course content.


#   This program displays step-by-step instructions
#   for making a sandwich.
#   The main function performs the program's main logic.
def main():
#   # Display the start-up message.
    startup_message()
    input('Press Enter to see Step 1.')
    # Display step 1.
    step1()
    input('Press Enter to see Step 2.')
    # Display step 2.
    step2()
    input('Press Enter to see Step 3.')
    # Display step 3.
    step3()
    input('Press Enter to see Step 4.')
    # Display step 4.
    step4()
    input('Press Enter to see Step 5.')
    # Display step 5.
    step5()
    input('Press Enter to see Step 6.')
    # Display step 6.
    step6()
    input('Press Enter to see Step 7.')
    # Display step 7.
    step7()
    goodbye_message()

    # The startup_message function displays the
    # program's initial message on the screen.
def startup_message():
    print('This program tells you how to make a sandwich.')
    print('There are 7 steps in the process.')
    print()
    # The goodbye_message function displays the
    # program's ending message on the screen.
def goodbye_message():
    print('Thanks for coming to my ted talk.')
    print('bye')
    print()
    
# The step1 function displays the instructions
# for step 1.
def step1():
    print('Get the following ingredients and supplies from your pantry:')
    print('Bread')
    print('Peanut butter')
    print('Jelly')
    print('Plate')
    print('Knife (butter or palette)')
    print()
# The step2 function displays the instructions
# for step 2.
def step2():
    print('Place two slices of bread on the plate side by side.')
    print()
# The step3 function displays the instructions
# for step 3.
def step3():
    print('Using the knife, spread as much jelly as desired on one slice of bread.')
    print('Be sure to wipe the remaining jelly off on the second slice, or on a paper towel.')
    print()
# The step4 function displays the instructions
# for step 4.
def step4():
    print('Using the cleaned knife, spread as much peanut butter as desired on the other slice of bread.')
    print()
# The step5 function displays the instructions
# for step 5.
def step5():
    print('Put the two pieces of bread together, jelly and peanut butter sides facing each other.')
    print()
# The step6 function displays the instructions
# for step 6.
def step6():
    print('Eat.')
    print()
    # The step7 function displays the instructions
# for step 7.
def step7():
    print(':::::THIS IS THE MOST IMPORTANT STEP:::::')
    print('Put your plate in the dishwasher, don\'t just leave it around the house.')
    print()
    
# Call the main function to begin the program.
main()