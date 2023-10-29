# Lab 5B –Value Returning Functions

# Falling Distance
# When an object is falling because of gravity, the following formula can be used to determine the distance the object falls in a specific time period:

# d = ½ gt2

# The variables in the formula are as follows:
# d is the distance in meters
# g is 9.8 (the gravitational constant)
# t is the amount of time in seconds the object has been falling

# Your program will calculate the distance in meters based on the object’s falling distance.

# Modularity:  Your program should contain 2 functions:
# main – will call the falling_distance function in a loop, passing it the values 1 – 10 as arguments (seconds the object has been falling).   It will display the returned distance.
# falling_distance – will be passed one parameter which is the time in seconds the object has been falling and will calculate and return the distance in meters.    falling_distance should be stored in a separate file (module) called distance.py   You will import distance before your main function in your original program file.
# Input Validation:  None needed
# Output:  Should look like this:
# Time	Falling Distance
# -----------------------------
# 1 	 4.90
# 2 	 19.60
# 3 	 44.10
# 4 	 78.40
# 5 	 122.50
# 6 	 176.40
# 7 	 240.10
# 8 	 313.60
# 9 	 396.90
# 10 	 490.00
# Programming Style Requirements.  
# 	•	Comments – Begin your program with a comment that includes: a) your name, b)program status – either “Complete” or describe any incomplete or non-functioning part of your program c)A 1-3 line description of what the program does.
# 	•	Function comments – each function should begin with a comment explaining what the function does
# 	•	Variable names – use meaningful variable names such as total_taxes or num_cookies.
# 	•	Function names – use meaningful verb names for functions such as display_taxes. 
# 	•	Named constants – Use named constants for all number values that will not be changed in the program such as RECIPE_SUGAR = 1.5.   See section 2.9 on Named Constants
# Your program file:    yourlastname_Lab5B.py 
#  Your distance module:   distance.py


# lexi scales, complete
# this program will calculate an objects falling distance in meters based on the object’s falling time.

import distance

# main – will call the falling_distance function in a loop, passing it the values 1 – 10 as arguments (seconds the object has been falling).   It will display the returned distance.
def main():
    # print header of table
    print('\nTime\tFalling')
    print('(sec)\tDistance (m)')
    print('------------------------')
    # loop 1-10
    for seconds in range(1,10):
        # call falling_distance function, passing in seconds
        fall_distance = distance.falling_distance(seconds)
        # print seconds and distance to table
        print(f'{seconds}\t{fall_distance:,.2f}')
    
# call main function
main()