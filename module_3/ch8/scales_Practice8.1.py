# Practice Assignment Ch. 8-1
# Write a program that does the following:
# 1. Accepts input of your first, last, and middle names into three separate strings
# 2. Concatenates them together to form a string called full_name
# 3. Counts the number of “a” or “A” letters
# 4. Counts the number of “e” or “E” letters
# 5. Counts the number of “s” or “S” letters
# 6. Displays each of the three counts
# Turn in your program to the practice assignment link in course content.


    # main() gets input for first middle and last name from user, concatenates them to a full name string, then counts the number of common letters, displaying the counts back to the user.
def main():
    # get user input for first, middle and last name
    first = str(input("Enter your first name: "))
    middle = str(input("Enter your middle name: "))
    last = str(input("Enter your last name: "))
    # concat inputs into full_name string
    full_name = first + middle + last
    # init vars for counts
    a_count = 0
    e_count = 0
    s_count = 0
    # loop through string
    for char in full_name:
        # count number of a/A letters in full_name
        if char.lower() == 'a':
            a_count += 1
        # count number of e/E letters in full_name
        if char.lower() == 'e':
            e_count += 1
        # count number of s/S letters in full_name
        if char.lower() == 's':
            s_count += 1
    # print counts of letters
    print('Common letter counts in full name')
    print(f'A:{a_count}')
    print(f'E:{e_count}')
    print(f'S:{s_count}')

if __name__ == '__main__':
    main()