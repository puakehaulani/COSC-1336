# lexi scales, complete
# this program will calculate an objects falling distance in meters based on the object’s falling time.

import distance

MIN_TIME = 1
MAX_TIME = 10

# main – will call the falling_distance function in a loop, passing it the values 1 – 10 as arguments (seconds the object has been falling).   It will display the returned distance.
def main():
    # print header of table
    print('\nTime\tFalling')
    print('(sec)\tDistance (m)')
    print('------------------------')
    # loop 1-10
    for seconds in range(MIN_TIME, MAX_TIME):
        # call falling_distance function, passing in seconds
        fall_distance = distance.falling_distance(seconds)
        # print seconds and distance to table
        print(f'{seconds}\t{fall_distance:,.2f}')
    
# call main function
main()