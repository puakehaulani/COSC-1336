# lexi scales, complete
# this program displays a chart of the total rise in ocean levels over the next 25 years, in milimeters
# it calculates the running total of the constant rate of rise over each year in a for loop

YEARLY_RISE = 1.8
total_rise = 0
print('\nOcean level rise over next 25 years, in milimeters\n')
print('Year\tRise(mm)')
print('~~~~~𖠳~~~~~~~~~~')
for year in range(25):
    total_rise += YEARLY_RISE
    print(f'{year + 1}\t{total_rise:.2f}')