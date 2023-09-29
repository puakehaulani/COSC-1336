# This is a comment line about this program
# The program is about fast food

hamburger = int(input('How much does a hamburger cost? $'))
fries = int(input('How much do fries cost? $'))
shake = int(input('How much does a shake cost? $'))

total_cost = hamburger + fries + shake

print(f'The total cost is ${total_cost:.0f}')

average_cost = total_cost / 3

print(f'The average cost is: ${average_cost:.0f}')