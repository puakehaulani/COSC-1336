# Practice Assignment Ch. 7-3
# 1. Write a program that contains a main function and a
# sub-function called total_list.
# 2. The main function will create two lists containing five
# integers (of your choosing) each
# 3. The main function will join the two lists together, sort
# the resulting 10 integer list, and pass it to the
# total_list function
# 4. The total_list function will total the integers in the
# list and return the total to the main function
# 5. The main function will print the list, print the total, and
# print the maximum and minimum values in the list.
# Turn in your program to the practice assignment
# link in course content.

def main():
    # create two lists containing five integers each
    list = [0, 6, 2, 1, 8]
    list2 = [6, 8, 1, 2, 1]
    # join the two lists together
    list += list2
    # sort resulting list
    list.sort()
    # call total list function, passing it new sorted list
    total = total_list(list)
    # print list
    print(f'Sorted list: {list}')
    # print total
    print(f'Total of list: {total:,}')
    # print max and min values in list
    print(f'Max: {max(list)}\tMin: {min(list)}')

def total_list(list):
    # instantiate total var
    total = 0
    # total integers in list
    for num in list:
        total += num
    # return total to main function
    return total

if __name__ == '__main__':
    main()