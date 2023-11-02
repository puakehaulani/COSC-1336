# Program 1 - Write numbers to a file:
# 1. Open an output file with the filename number_list.txt
# 2. Use a loop to write the numbers 50 through 100 to the
# file, and then close the file. Be sure to save your file to
# use in the next assignment


# This program creates a file with the numbers 50-100

def main():
    # open output file with filename number_list.txt
    outfile = open('number_list.txt', 'w')
    # use a loop to write the numbers 50 through 100 to the file
    MIN_NUM = 50
    MAX_NUM = 100
    for number in range(MIN_NUM, MAX_NUM +1):
        outfile.write(f'{str(number)}\n')
    # close the file
    outfile.close()

if __name__ == '__main__':
    main()