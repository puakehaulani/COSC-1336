# Practice Assignment Ch. 9-2
# Still in the groups from last class (online students do remainder of assignment), using
# the dictionary application you created, add two new menu items:
#  Save the dictionary – write a function to pickle the dictionary to a file
#  Retrieve the dictionary – write a function to retrieve the pickled
# dictionary that was saved earlier
#  Put both functions in a separate module that is imported by your main
# program
# Turn in your programs/modules to the practice assignment link in
# course content.

def save_dictionary():
    # open file
    outfile = open('dogfarm.txt', 'w')
    # write data to file
    
    # close file
    outfile.close()

def get_dictionary():
    # open file
    infile = open('dogfarm.txt', 'r')
    # retrieve data
    
    # close file
    infile.close()
