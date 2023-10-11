# 1. In Python, use your if-elif-else program from Practice Assignment 3-2,
#       that asks for a number and prints the day of the week.
#       Add logic to this program that uses a loop to keep asking the user the day of the week until they wish to stop.
#       You will use a while loop to do this.
keep_going = 'y'
while keep_going == 'y':
    number = int(input('Please choose a number in the range of 1-7: '))
    if number == 1:
        print(f'{number} means Monday')
    elif number == 2:
        print(f'{number} means Tuesday')
    elif number == 3:
        print(f'{number} means Wednesday')
    elif number == 4:
        print(f'{number} means Thursday')
    elif number == 5:
        print(f'{number} means Friday')
    elif number == 6:
        print(f'{number} means Saturday')
    elif number == 7:
        print(f'{number} means Sunday')
    else:
        print('Error: Invalid Entry')
    keep_going = input('Do you want to keep going? Enter y for yes: ')
    
