# 1. Write a program that opens an output file with the filename my_name.txt,
# writes your name to the file, then someone else’s name. Then, write your age to
# the file. Close the file.
# 2. Open my_name.txt in notepad and view the contents.


# This program writes personal data to a file

def main():
    # open a file called my_name.txt
    outfile = open('my_name.txt', 'w')
    # write my name to the file
    outfile.write('lexi scales\n')
    # write someone elses name to the file
    outfile.write('lady scales\n')
    # write my age to the file
    outfile.write('34\n')
    # close the file
    outfile.close()

if __name__ == '__main__':
    main()
    
