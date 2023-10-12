# lexi scales, program complete
# This is a budgeting program. The user enters their monthly budget, and then is prompted to enter expenses. The program totals their expenses, and tells them if they were over or under budget, and by how much.

print('Budgeting Program')
total_expenses = 0
budget = float(input('Enter amount budgeted for the month: '))
while budget < 0:
    print('Error: Invalid entry. Enter a positive number.')
    budget =float(input('Enter amount budgeted for the month: '))
expense = float(input('Enter an amount spent(0 to quit): '))
while expense != 0:
    total_expenses += expense
    expense = float(input('Enter an amount spent(0 to quit): '))
difference = budget - total_expenses
print(f'Budgeted: ${budget:,.2f}')
print(f'Spent: ${total_expenses:,.2f}')
if difference < 0:
    print(f'You are ${abs(difference):,.2f} over budget (ㅠ﹏ㅠ)')
else:
     print(f'You are ${difference:,.2f} under budget (੭˃ᴗ˂)੭')

