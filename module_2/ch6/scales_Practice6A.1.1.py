# Write a program that opens the my_name.txt file that was created by the
# program in problem 1, reads the names from the file, displays the names on the
# screen. Read your age and divide it by two. Print both age and age divided by 2
# and then close the file. Don’t forget to strip off the newline character when you
# read in the names and convert the age to int.


# This program reads and displays personal data from a file

def main():
    # open my_name.txt
    infile = open('my_name.txt', 'r')
    # read names from the file
    name1 = infile.readline()
    name2 = infile.readline()
    # read age
    age = int(infile.readline())
    # close file
    infile.close()
    # print names
    print(f'names: {name1.rstrip()}, {name2.rstrip()}')
    # divide age by 2
    halfAge = age/2
    # print age
    # print age/2
    print(f'age: {age}\nage / 2: {halfAge:.1f}')
    
if __name__ == '__main__':
    main()