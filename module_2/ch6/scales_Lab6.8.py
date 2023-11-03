# 8 Random Number File Reader
# This exercise assumes you have completed Programming Exercise 7. Write another program that reads the random numbers from the file, displays the numbers, then displays the following data:
#   The total of the numbers
#   The number of random numbers read from the file
#   The average of the random numbers

# Exception Handling:   Both programs should use Try and Except Clauses to handle IOError, ValueError, and unspecified error exceptions.   Be sure to test your programs for invalid cases.  For example ,  try running the second program to read the file when it doesn’t exist or manually put bad data in the file and see what happens.  

# Programming Style Requirements.  
# 	•	Comments – Begin your program with a comment that includes: a) your name, b)program status – either “Complete” or describe any incomplete or non-functioning part of your program c)A 1-3 line description of what the program does.
# 	•	Function comments – each function should begin with a comment explaining what the function does
# 	•	Variable names – use meaningful variable names such as total_taxes or num_cookies.
# 	•	Function names – use meaningful verb names for functions such as display_taxes. 
# 	•	Named constants – Use named constants for all number values that will not be changed in the program such as RECIPE_SUGAR = 1.5.   See section 2.9 on Named Constants

# You should have 2 program files to turn in.

# lexi scales. incomplete.
# this program reads a file of numbers then displays the numbers, their sum, and the amount of numbers read from the file.

# this is the main function of the program. it contains the program logic. 
def main():
    # initialize sum var
    sum = 0
    # initialize count var
    count = 0
    # try suite
    try:
        pass
        # open file
        infile = open('random_number_list', 'r')
        # for loop to read contents
        for line in infile:
            # add one to count
            count += 1
            # convert line to integer
            number = int(line)
            # add number to sum
            sum += number
        # close file
        infile.close()
    # exception for IOError
    except IOError as err:
        print("\tERROR: {err}\n\tThere was a problem reading file")
    # exception for ValueError
    except ValueError as err:
        print("\tERROR: {err}\n\tRecord is not a valid number")
    # unspecified exception error
    except Exception as err:
        print("\tERROR: {err}\n\tAn error occurred")
        
    average = sum/count
    print(f'The sum of the valid numbers in this file is {sum:,}')
    print(f'The amount of the valid numbers in this file is {count:,}')
    print(f'The average of the valid numbers in this file is {average:,.2f}')
  
if __name__ == '__main__':
    main()