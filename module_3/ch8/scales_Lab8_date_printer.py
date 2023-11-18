# Problem 2.  Date Printer - Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.   It should print the date in the format March 12, 2018.  

# Sample dialog:
# Enter a date in the format mm/dd/yyyy: 01/16/2018
# January 16, 2018

# You should have 2 .py files to turn in.   


# lexi scales, incomplete.
# this program reads a string from the user containing a date in the form mm/dd/yyyy, and converts it to be printed in format Month day, year.

import re
import datetime

def main():
    # enter_date function, with return saved to var
    user_date = enter_date()
    print(user_date)
    # format to Month day, year
    
    # print new format
    
# enter_date prompts a user to enter a date then verifies it is a valid date in the format specified. it handles exceptions by rerunning the function. it returns the valid date object.
def enter_date():
    try:
    # user enters date in format mm/dd/yyy
        date_input = str(input('Enter a date in the format mm/dd/yyy: '))
    # verify entry meets format
        datetime.datetime.strptime(date_input, '%m/%d/%Y')
        return date_input
    except Exception as err:
        print(f'Error: {err}')
        return enter_date()
    
if __name__ == '__main__':
    main()