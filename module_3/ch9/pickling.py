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

import pickle


def save_dictionary(dictionary, filename):
    # open file
    outfile = open(filename, 'wb')
    # pickle data to file
    pickle.dump(dictionary, outfile)
    # print confirmation
    print('Dictionary saved to {filename}') 
    # close file
    outfile.close()

def get_dictionary(filename):
    end_of_file = False
    try:
        # open file
        infile = open(filename, 'rb')
        while not end_of_file:
            print('File data:')
            # unpickle data
            content = pickle.load(infile)
            if len(content) == 0:
                print("No data")
            # print in a readable format
            for line in content:
                # display data
                print(line.capitalize(), content[line].capitalize())
                # end condition
            end_of_file = True
        
        # close file
        infile.close()
    # exception for IOError
    except IOError as err:
        print("\tERROR: {err}\n\tThere was a problem reading file")
    # unspecified exception error
    except Exception as err:
        print(f"\tERROR: {err}\n\tAn error occurred")