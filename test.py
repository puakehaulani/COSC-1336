import math
def calc_circle_is_bigger_than_square(radius, length):
    circle_area = math.pi * radius **2
    square_area = length **2
    if circle_area > square_area:
        circle_bigger = True
    else:
        circle_bigger = False
    return circle_bigger, circle_area, square_area

def main():
    display = calc_circle_is_bigger_than_square(25, 10)
    print(display)
    
main()