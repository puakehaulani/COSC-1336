# 2. In a second program:
#       Write a while loop that asks the user to enter two numbers.
#       The numbers should be added and the sum displayed.
#       The loop should ask the user if he or she wishes to perform the operation again.
#       If so, the loop should repeat, otherwise it should terminate.

again = 'y'
while again == 'y':
    print('Enter two numbers to get their sum')
    number1 = int(input('First number: '))
    number2 = int(input('Second number: '))
    sum = number1 + number2
    print(f'The sum is {sum}')
    again = input('Do you want to add another set? Enter y for yes: ')