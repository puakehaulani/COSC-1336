# 1. Write a program that uses the file you created in 6 – 2 called
# number_list.txt
# 2. Your program should read in number_list.txt and calculate the sum and
# average of all the numbers and display the sum and the average.
# 3. Additionally, it should:
# a. Handle any IOError exceptions that are raised when the file is opened and
# data is read from it
# b. Handle any ValueError exceptions that are raised when the items read are
# converted to numbers
# c. Handle any other unspecified errors
# Turn in your program to the practice assignment link in course content.


# this program reads a file of numbers, calculates the sum and average of the numbers, and displays these amounts.
def main():
    # initialize counter var
    count = 0
    # initialize sum var
    sum = 0
    # try suite
    try: 
    # open file
        infile = open('number_list.txt', 'r')
        # for loop to go through each line
        for line in infile:
            # add one to the counter var
            count += 1
            # convert the number to an int and add number to the sum var
            num = int(line)
            sum += num
        # close file
        infile.close()
        print('╭── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ──╮')
        # print the sum
        print(f'the sum of the valid numbers in this file is {sum:,}')
        # print the average (sum/count)
        average = sum/count 
        print(f'the average of the valid numbers in this file is {average:,.2f}')
        print('╰── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ── ⋅ ⋅ ──╯')
    # IOError exceptions
    except IOError as err:
        print(f'\tERROR: Problem reading file\n\t{err}')
    # ValueError exceptions
    except ValueError as err:
        print(f'\tERROR: Record is not a valid number\n\t{err}')
    # unspecified errors
    except Exception as err:
        print(f'\tERROR: An error has occurred\n\t{err}')

        
if __name__ == '__main__':
    main()