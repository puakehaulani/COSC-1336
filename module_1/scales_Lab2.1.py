# lexi scales. program complete.
# this program that asks the user how many servings of spaghetti sauce they want to make,
# then displays the amount of each ingredient needed for the specified number of servings.

# Set constant for one serving of tomato sauce
TOMATO_SAUCE_SINGLE_SERVING = 0.5
# Set constant for one serving of tomato paste
TOMATO_PASTE_SINGLE_SERVING = .08325
# Set constant for one serving of garlic cloves
GARLIC_SINGLE_SERVING = 0.5
# Set constant for one serving of oregano
OREGANO_SINGLE_SERVING = 0.25

# Ask user to input number of servings they want to make, set it to a 'servings' variable
servings = int(input('How many servings of spgahetti sauce do you need to make? '))

# Multiply tomato sauce const by servings, assign to variable
tomato_sauce_needed = TOMATO_SAUCE_SINGLE_SERVING * servings
# Multiply tomato paste const by servings, assign to variable
tomato_paste_needed = TOMATO_PASTE_SINGLE_SERVING * servings
# Multiply garlic clove const by servings, assign to variable
garlic_needed = GARLIC_SINGLE_SERVING * servings
# Multiply oregano const by servings, assign to variable
oregano_needed = OREGANO_SINGLE_SERVING * servings

# Print full recipe with amount of each ingredient for the servings variable number of servings, rounded to 2 decimal places
# Format print statement to be easily readable

print('\n┌──────────────────────── •✧• ────────────────────────┐\n'
    f'\nFor {servings} servings of spaghetti sauce, you will need:\n'
      f'{tomato_sauce_needed:10.2f} C'
      f'{"Tomato Sauce":>21}\n'
      f'{tomato_paste_needed:10.2f} C'
      f'{"Tomato Paste":>21}\n'
      f'{garlic_needed:10.2f} cloves'
      f'{"Garlic":>10}\n'
      f'{oregano_needed:10.2f} TBSP'
      f'{"Oregano":>13}\n'
      '\nHappy cooking!\n'
      '\n╰─────────────────────────────────────────────────────╯'
      ), 
