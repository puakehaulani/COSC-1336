# Practice Assignment Ch. 7-4
# Write a program that creates a two dimensional list with 4
# rows and 3 columns.
# 1. Write a nested loop to get an integer value from the user
# for each element in the list.
# 2. Write another nested loop to sum and display each
# element in the list.
# 3. Print the total of all elements
# Turn in your program to the practice assignment link in
# course content.


def main():
    pass
    ROWS = 4
    COLS = 3
    # init sum var
    sum = 0
    # create 2d list with 4 row and 3 col
    two_d_list = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
    # write nested loop to get int value from user for each element in list
    for r in range(ROWS):
        for c in range(COLS):
            two_d_list[r][c] = int(input('Please enter an integer: '))
    # write nested loop to sum and display each element
    for row in two_d_list:
        for element in row:
            sum += element
            print(element)
    # print sum
    print(f'The total of all the elements is {sum}')
    
if __name__ == '__main__':
    main()