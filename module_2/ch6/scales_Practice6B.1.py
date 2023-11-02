# 1. Write a program that uses the file, students.txt. The file contains several records. Each record contains two
# fields: 1) the student’s name and 2) the student’s score for the final exam.
# 2. Your program should read in each record in students.txt using a loop.
# 3. While in the loop, the program should display name and score
# 4. Sample output:
# Name Score
# --------------------------------
# Jim Smith 99.0
# Mario Alvarez 100.0
# Mary Maldonado 89.0
# Bess Robinson 77.0
# Eddie Nguyen 87.0
# Turn in your program to the practice assignment link in course content.

# this program reads a file with student records. it reads through the records and displays the content

def main():
    # print header
    print(f'Name\t\tScore')
    print('-----------------------')
    # open file
    infile = open('students.txt', 'r')
    # read first records name field
    name = infile.readline()
    # read rest of the file
    while name != '':
        # read the score field
        score = float(infile.readline())
        # strip newline from name
        name = name.rstrip('\n')
        # display name and score on one line
        print(f'{name}\t{score:.1f}')
        # read next record
        name = infile.readline()
    # close file
    infile.close()
if __name__ == '__main__':
    main()