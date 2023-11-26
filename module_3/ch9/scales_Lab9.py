# lexi scales, incomplete
# this program contains dictionaries with class information. a user enters a course number and it will display the course information. a user can continue entering course numbers until they quit the program.

# create dictionary with course numbers and room numbers for the course
course_room_dict = {
    'cs101': 3004,
    'cs102': 4501,
    'cs103': 6755,
    'nt110': 1244,
    'cm241': 1411,
}

# create dictionary for course numbers and instructor name for the course
course_instructor_dict = {
    'cs101': 'Haynes',
    'cs102': 'Alvarado',
    'cs103': 'Rich',
    'nt110': 'Burke',
    'cm241': 'Lee',
}

# create dictionary for course numbers and meeting time for the course
course_time_dict = {
    'cs101': '8:00 a.m.',
    'cs102': '9:00 a.m.',
    'cs103': '10:00 a.m.',
    'nt110': '11:00 a.m.',
    'cm241': '1:00 p.m.',
}

# main
# loop while quit != true
    # get user input (course number or quit)
    # check if course is valid
        # if valid, display course info from dictionaries
        # if not valid, display error message