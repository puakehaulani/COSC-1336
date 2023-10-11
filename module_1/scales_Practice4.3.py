# Square Display
# Write a program that:
# 1. Asks the user for a positive integer no greater than 15 (use input
# validation).
# 2. Asks the user for a character to use to create the square.
# 3. The program should display a square on the screen with the
# number of rows and columns entered by the user using the
# character provided by the user.
# 4. For example if the user enters 5 and % the output should be
# %%%%%
# %%%%%
# %%%%%
# %%%%%
# %%%%%
# 5. Turn in your program to the practice assignment link in course
# content.
print('Creating a rectangle')
integer = int(input('Please enter positive integer no greater than 15: '))
while integer < 0 or integer > 15:
    print('ERROR: The integer cannot be negative or greater than 15.')
    integer = int(input('Please enter a valid number: '))
character = str(input('Please enter a character to create the rectangle: '))
for row in range(integer):
    for col in range(integer):
        print(character, end='')
    print()