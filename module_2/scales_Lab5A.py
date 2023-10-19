# Lab 5A –Void Functions

# Average Restaurant Rating and Number of Stars – A restaurant receives numeric scores of 0-10 from five different food critics. The higher the score, the better the rating.  The average score translates into a 1 – 5 star rating.  
# Write an IPO diagram and Python program that has two functions, main and determine_stars.
# main – Should accept input of five numeric ratings from the user USING A LOOP.   It should then calculate the average numeric score for the restaurant.    The numeric average should be passed to the determine_stars function.

# determine_stars  – should display the number of stars based on the numeric average:

#        Greater than 9:   *****
# 8.0 - 8.9:   	 ****
# 7.0 – 7.9:              ***
# 6.0 – 6.9:              **
# 5.0 – 5.9:  	  *
# Below 5.0             No stars

# Design:
# Design your program logic using pseudocode in the attached IPO Diagram.  You should have 2 separate diagrams.  One for the main function and one for the determine_stars  function.

# Modularity:  Your program should contain 2 functions:   a main function to accept input from the user and calculate average and a second function to display the number of stars.
# Input Validation:  The test scores entered by the user should be in the range 0-10
# Output:   Display both the numeric average (rounded to two decimals) and the number of stars.
# Sample Dialog:   
# Enter critic's score between 0 and 10: -1
# Error: Enter critic's score between 0 and 10: 5
# Enter critic's score between 0 and 10: 6
# Enter critic's score between 0 and 10: 7
# Enter critic's score between 0 and 10: 8
# Enter critic's score between 0 and 10: 9
# Your score of 7.0 gives you ***
# >>>
# Programming Style Requirements.  
# 	•	Comments – Begin your program with a comment that includes: a) your name, b)program status – either “Complete” or describe any incomplete or non-functioning part of your program c)A 1-3 line description of what the program does.
# 	•	Function comments – each function should begin with a comment explaining what the function does
# 	•	Variable names – use meaningful variable names such as total_taxes or num_cookies.
# 	•	Function names – use meaningful verb names for functions such as display_taxes. 
# 	•	Named constants – Use named constants for all number values that will not be changed in the program such as RECIPE_SUGAR = 1.5.   See section 2.9 on Named Constants

# You should have 2 files to turn in:  
# Your program file:    yourlastname_Lab5A.py 
# Your IPO diagram:   yourlastname_Lab5A_IPO.docx
