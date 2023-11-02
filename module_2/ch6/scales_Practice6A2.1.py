# Program 2 – Read numbers from a file:
# 1. Open the file you just created.
# 2. Read all the numbers from the file and display them.
# Terminate the loop by detecting end of file with a for loop
# (the second method we discussed).
# Turn in your two program files to the practice assignment link
# in course content.

# this program reads numbers from a file and displays them

def main():
    # open file
    infile = open('number_list.txt', 'r')
    # read first line
    line = infile.readline()
    # while there are lines in the file, read the contents
    while line != '':
        # convert line to integer
        num = int(line)
        # print line
        print(f'{num}')
        # read next line
        line = infile.readline()
    # close file
    infile.close()
    

if __name__ == '__main__':
    main()