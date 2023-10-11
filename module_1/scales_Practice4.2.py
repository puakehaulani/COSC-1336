# In Python - Write a program that asks the user to enter two numbers, a low number
# and a high number. The program will contain two for loops:
#       1. In the first loop, the low number will be the starting point for the loop and the
#       high will be the ending point. The loop should display the iterator number and
#       that number x 10 on the same line, separated by a tab. See example on p. 177.
#       2. The second loop should accumulate all the numbers between the starting point
#       and ending point. You will need to create and initialize an accumulator such as
#       total before you start the loop.
# Turn in your program to the practice assignment link in course
# content.


print('This program creates a table of numbers and their multiple of ten. It needs a low number and a high number to run.')
low_number = int(input('Low number: '))
high_number = int(input('High number: '))
print('Number\tMultiple')
print('==============')
for number in range(low_number, high_number):
    multiplied = number * 10
    print(f'{number}\t{multiplied}')
total = 0
for number in range(low_number, high_number):
    total += number
print(f'Total accumulated numbers: {total}')

