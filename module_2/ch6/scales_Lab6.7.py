# Lab 6 – Files:  Random Numbers 

# You will create each program in the IDLE environment and save it as a python file.  Use the file naming convention yourlastname_Lab6.n.py  where “n” is the exercise number.

# 7 Random Number File Writer
# Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold.


# Programming Style Requirements.  
# 	•	Comments – Begin your program with a comment that includes: a) your name, b)program status – either “Complete” or describe any incomplete or non-functioning part of your program c)A 1-3 line description of what the program does.
# 	•	Function comments – each function should begin with a comment explaining what the function does
# 	•	Variable names – use meaningful variable names such as total_taxes or num_cookies.
# 	•	Function names – use meaningful verb names for functions such as display_taxes. 
# 	•	Named constants – Use named constants for all number values that will not be changed in the program such as RECIPE_SUGAR = 1.5.   See section 2.9 on Named Constants

# You should have 2 program files to turn in.


# lexi scales. complete.
# this program writes a series of random numbers to a file. each random number is between 1 and 500. the user will determine how many random numbers the file should have. 

import random

# this is the main function of the program. it holds the program logic.
def main():
    # initialize var for min and max number
    MIN_VAL = 1
    MAX_VAL = 500
    # get users input on amount of numbers to add to the file
    amount = int(input('How many random numbers do you want to add to the new file?  '))
    # open file
    outfile = open('random_number_list', 'w')
    # for loop 
    for line in range(1, amount + 1):
    # add the number to the file in string form
        outfile.write(f'{str(random.randint(MIN_VAL, MAX_VAL))}\n')
    # close file
    print(f'file created with {amount} lines')
    outfile.close()

if __name__ == '__main__':
    main()