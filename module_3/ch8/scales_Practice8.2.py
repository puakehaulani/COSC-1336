# Practice Assignment Ch. 8-2
# 1. Flip case: Write a program to do the following:
# 2. Accept the input of a sentence from the user that contains lowercase, uppercase,
# and special characters.
# 3. Make a new sentence in which the lowercase characters are changed to
# uppercase and the uppercase are changed to lower case. All other characters will
# retain their original value.
# 4. Print the original sentence and the new sentence.
# 5. Turn in your program to the practice assignment link in course
# content.

# main() switches the casing of letters in a string. uppercase become lowercase, lowercase become uppercase. other characters are unchanged.
def main():
    pass
    # get user input of a sentence containing uppercase, lowercase, and special char
    original_sentence = str(input('Input a sentence here. Please include lowercase, uppercase, and special characters.\n'))
    # create copy of string with case flipped
    flipped_sentence = None
    # print original sentence
    print(f'Original sentence:\n{original_sentence}')
    # print new sentence
    print(f'Flipped sentence:\n{flipped_sentence}')


if __name__ == '__main__':
    main()