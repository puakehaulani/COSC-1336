# lexi scales, program complete
# this program calculates bulk discount amounts for Geekware Software Company packages.
# the user enters the number of packages they purchased, and the program will calculate then display the dollar amount of the discount, if any, and the total cost of the order after discount.

BASE_PRICE = 149
number_purchased = int(input('Enter the number of packages purchased: '))

if number_purchased < 10:
    discount = 0
elif number_purchased < 50:
    discount = .1
elif number_purchased < 100:
    discount = .2
elif number_purchased < 150:
    discount = .3
else:
    discount = .4
    
discount_amount = (number_purchased * BASE_PRICE) * discount
total_amount = (number_purchased * BASE_PRICE) - discount_amount

print(f'Discount Amount: ${discount_amount:,.2f}')
print(f'Total Amount: ${total_amount:,.2f}')

