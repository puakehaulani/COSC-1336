# lexi scales, program complete
# this program calculates bulk discount amounts for Geekware Software Company packages.
# the user enters the number of packages they purchased, and the program will calculate then display the dollar amount of the discount, if any, and the total cost of the order after discount.

BASE_PRICE = 149
number_purchased = int(input('Enter the number of packages purchased: '))
bulk_10 = 10
bulk_50 = 50
bulk_100 = 100
bulk_150 = 150
percent_10 = 0
percent_50 = .1
percent_100 = .2
percent_150 = .3
percent_max = .4

if number_purchased < bulk_10:
    discount = percent_10
elif number_purchased < bulk_50:
    discount = percent_50
elif number_purchased < bulk_100:
    discount = percent_100
elif number_purchased < bulk_150:
    discount = percent_150
else:
    discount = percent_max
    
discount_amount = (number_purchased * BASE_PRICE) * discount
total_amount = (number_purchased * BASE_PRICE) - discount_amount

print(f'Discount Amount: ${discount_amount:,.2f}')
print(f'Total Amount: ${total_amount:,.2f}')

