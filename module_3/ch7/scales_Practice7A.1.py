# Practice Assignment Ch. 7-1
# 1. Lottery number generator: Write a program that generates a
# seven-digit lottery number. The program should have a loop
# to generate seven random numbers, each in the range 0
# through 9 and assign each number to a list element.
# 2. Write another loop to display the contents of the list.
# 3. Tip: You will need to create/initialize your list before you can
# assign numbers to it.
# 4. Use program 7-1 sales_list as an example. You will start with
# a seven-digit lottery number that contains all zeros. Then in
# your loop, you will assign a random number instead of
# getting the data from the user.
# Turn in your program to the practice assignment link in course
# content.

import random 

def main():
    POSSIBLE_NUMBERS = 7
    # initialize list with 7 entries
    lottery_numbers = [0] * POSSIBLE_NUMBERS
    try:
         # loop through list and assign each a random number 0-9
         for index in range(len(lottery_numbers)):
             lottery_numbers[index] = random.randint(0,9)
    except IndexError as err:
        print('Error, {err}')
    except Exception as err:
        print('Error, {err}')
    # loop to display contents of list
    print('Your lottery number is:')
    for number in lottery_numbers:
        print(number)


if __name__ == '__main__':
    main()