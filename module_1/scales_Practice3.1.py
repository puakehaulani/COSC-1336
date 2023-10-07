# Magic Dates
# The date June 10, 1960 is special because when it is written in the following format, the months times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a two digit year. The program should then determine whether the month times the day equals the year. If so, it should display a message saying the date is magic. Otherwise, it should display a message saying the date is not magic.
print('This is the Magic Date program. Enter a date to see if it is --✧*̥˚ magic *̥˚✧--')
month = int(input('Please enter the month, in numeric format: '))
day = int(input('Please enter the day: '))
year = int(input('Please enter the year, using just the last two digits (ex: for 2023, you would enter 23): '))

if month * day == year:
    print('This date is °˖✧MAGiC✧˖°')
else:
    print('This date is NOT magic ( •̯́ ₃ •̯̀) ')