# lexi scales. complete.
# this program reads a file of numbers then displays the numbers, their sum, and the amount of numbers read from the file.

# this is the main function of the program. it contains the program logic. 
def main():
    # initialize sum var
    sum = 0
    # initialize count var
    count = 0
    # try suite
    try:
        pass
        # open file
        infile = open('random_number_list', 'r')
        # for loop to read contents
        for line in infile:
            # add one to count
            count += 1
            # convert line to integer
            number = int(line)
            # add number to sum
            sum += number
        # close file
        infile.close()
    # exception for IOError
    except IOError as err:
        print("\tERROR: {err}\n\tThere was a problem reading file")
    # exception for ValueError
    except ValueError as err:
        print("\tERROR: {err}\n\tRecord is not a valid number")
    # unspecified exception error
    except Exception as err:
        print("\tERROR: {err}\n\tAn error occurred")
        
    average = sum/count
    print(f'The sum of the valid numbers in this file is {sum:,}')
    print(f'The amount of the valid numbers in this file is {count:,}')
    print(f'The average of the valid numbers in this file is {average:,.2f}')
  
if __name__ == '__main__':
    main()