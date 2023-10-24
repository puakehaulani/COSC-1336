# In Python, write a program to generate a random floating point number between 1
# and 100 which will be used as the radius of a circle. In a separate function, calculate
# the area of a circle based on the radius your program just generated and return it to
# the main function. In the main function, display the radius and the area.
# Turn in your program to the practice assignment link in course content.

import random
import math

MIN = 1
MAX = 100
# the main function runs the program. it generates a number as a radius, calls an area calculating function, then displays the radius and area.
def main():
    print('≪°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。≫')
    print('\nThis program generates a random number 1-100 as a radius,\nthen calculates the area of the circle and displays the results for you.\n')
    # generate random float 1-100, name radius
    radius = random.uniform(MIN,MAX)
    # call area function, pass radius
    area = calculate_area(radius)
    # print radius and area
    print(f'This random circle\'s radius is {radius:.2f} and its area is {area:,.2f}\n')
    print('≪°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。°。≫')
# the calculate_area function calculates the area of a circle based on the radius prop
def calculate_area(radius):
    return math.pi * radius**2

main()