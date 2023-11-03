# lexi scales. complete.
# this program writes a series of random numbers to a file. each random number is between 1 and 500. the user will determine how many random numbers the file should have. 

import random

# this is the main function of the program. it holds the program logic.
def main():
    # initialize var for min and max number
    MIN_VAL = 1
    MAX_VAL = 500
    # get users input on amount of numbers to add to the file
    amount = int(input('How many random numbers do you want to add to the new file?  '))
    # open file
    outfile = open('random_number_list', 'w')
    # for loop 
    for line in range(1, amount + 1):
    # add the number to the file in string form
        outfile.write(f'{str(random.randint(MIN_VAL, MAX_VAL))}\n')
    # close file
    print(f'file created with {amount} lines')
    outfile.close()

if __name__ == '__main__':
    main()