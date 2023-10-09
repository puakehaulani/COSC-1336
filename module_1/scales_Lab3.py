# Lab 3 Decision Structures

# Problem 1.  Volume Discounts
# Geekware Software Company’s biggest seller software package sells for $149 each.  Quantity discounts are given according to the following table:
# Quantity 
# Discount
# 10-49
# 10%
# 50-99
# 20%
# 100-149
# 30%
# 150 or more
# 40%

# Write a program that asks the user to enter the number of packages purchased.  The program should then display the dollar amount of the discount (if any) and the total amount of the purchase after discount.
# See Section 3.4 for information and examples of nested decision structures and multiple nested decision structures.
# Code.  Write your program in Python using the above steps. Save your program as a .py file with the name yourlastname_Lab3.py 
# Output.  Your program should produce correctly labeled output with dollar amounts rounded to 2 decimal places and dollar signs displayed.  See section 2.8 More About Output.  Sample dialog:
# Enter the number of packages purchased: 53
# Discount Amount: $ 1,579.40
# Total Amount: $ 6,317.60


# lexi scales, program status
# This program calculates bulk discount amounts for Geekware Software Company packages.
# The user enters the number of packages they purchased, and the program will calculate then display the dollar amount of the discount, if any, and the total cost of the order after discount.

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

