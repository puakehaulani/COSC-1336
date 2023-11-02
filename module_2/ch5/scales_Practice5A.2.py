# 1. Kilometer Converter - Write a program that asks the user to enter a
# distance in kilometers, and then converts that distance to miles. The
# conversion formula is as follows:
# Miles = Kilometers x 0.6214
# 2. Your program should have two functions: a main function and a function
# to convert and print the miles
# 3. The main function should ask the user for number of kilometers and pass
# that to the conversion function.
# 4. The conversion function should calculate the miles and then display to
# user
# 5. Use a global constant for the conversion factor
# 6. Turn in your program to the practice assignment link in course content.

# This program converts kilometers to miles
CONVERSION_RATE = 0.6214
def main():
    start_message()
    kilometers = float(input('Enter number of km: '))
    conversion(kilometers)
    goodbye_message()


def start_message():
    print('This program converts kilograms to miles')


def conversion(kilometers):
    print(f'\nThere are {kilometers * CONVERSION_RATE:,.2f} mi in {kilometers} km\n')
    
def goodbye_message():
    print('Hope that helped!')
    
main()