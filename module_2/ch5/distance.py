# lexi scales. complete
# this program calculates the distance an object has fallen in meters based on the falling time in seconds.

# When an object is falling because of gravity, the following formula can be used to determine the distance the object falls in a specific time period:
# d = ½ gt^2
# The variables in the formula are as follows:
# d is the distance in meters
# g is 9.8 (the gravitational constant)
# t is the amount of time in seconds the object has been falling


# falling_distance – will be passed one parameter which is the time in seconds the object has been falling and will calculate and return the distance in meters.
def falling_distance(time):
    GRAVITY_CONST = 9.8
    MULTIPLIER_CONST = 1/2
    distance = MULTIPLIER_CONST * GRAVITY_CONST * time**2
    return distance
