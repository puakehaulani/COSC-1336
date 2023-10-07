# In IDLE – do the following, print and turn in when you are done:
# 1. Write a program that asks the user for a number in the range of 1-7. The program
# should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
# 3 = Wednesday, etc.
# 2. If the user enters anything except the numbers 1-7, an error message should be
# displayed.
# 3. Write two programs: one that uses if-else-if logic and the second uses if-elif-else
# 4. Turn in your program to the practice assignment link in course content.

number = int(input('Please choose a number in the range of 1-7: '))

# if-else-if program
print('if-else-if program result:')
if number == 1:
    print(f'{number} means Monday')
else:
    if number == 2:
         print(f'{number} means Tuesday')
    else:
        if number ==3:
            print(f'{number} means Wednesday')
        else:
            if number == 4:
                print(f'{number} means Thursday')
            else:
                if number == 5:
                    print(f'{number} means Friday')
                else:
                    if number == 6:
                        print(f'{number} means Saturday')
                    else:
                        if number == 7:
                            print(f'{number} means Sunday')
                        else:
                            print('Error: Invalid Entry')
                            
# if-elif-else program
print('if-elif-else program result:')
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
    