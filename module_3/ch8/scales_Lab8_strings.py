# lexi scales, complete
# this program reads a file, counts the types of characters it contains, and then prints them to the user.

def main():
    # init count vars (uppercase, lowercase, digits, whitespaces)
    upper = 0
    lower = 0
    digit = 0
    whitespace = 0
    # open file
    infile = open('text.txt', 'r')
    # read file, save to a string
    file_contents = infile.read()
    # close file
    infile.close()
    # loop through each char in the string
    for ch in file_contents:
    # if uppercase
        if  ch.isupper():
            # add to uppercase count
            upper += 1
        # elif lowercase
        elif ch.islower():
            # add to lowercase count
            lower += 1
        # elif digit
        elif ch.isdigit():
            # add to digit count
            digit += 1
        # elif whitespace
        elif ch.isspace():
            # add to whitespace count
            whitespace += 1
    # print each count
    print('Here\'s what I found about the content in this file:')
    print(f'Uppercase letters: {upper}\nLowercase letters: {lower}\nDigits: {digit}\nSpaces: {whitespace}')

if __name__ == '__main__':
    main()
  


