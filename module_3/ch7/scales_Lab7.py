# lexi scales. complete.
# this program displays all numbers in a list that are greater than a chosen number (n)

def main ():
    # main – should accept input of a series of 10 integers from the user and an integer n that will be the search number.  main should call the function display_larger and pass 2 arguments:   the 10 integers stored in a list, and the number n.
    # This function should display:   The original list, n, and the list of numbers greater than n.
  
    # constant for amount of numbers in list
    SIZE = 10
    # init empty list
    num_list = [0] * SIZE
    print('Enter a list of 10 integers')
    # loop to input 10 integers
    for index in range(len(num_list)):
        num_list[index] = enter_num()
    # input n search number
    print('Enter the number to search for:')
    n = enter_num()

    # call display_larger
    larger_list = display_larger(num_list, n)
    
    # print n
    print(f'Number: {n}')
    # print original list
    print(f'List of numbers:\n{num_list}')
    # print larger list 
    print(f'List of numbers that are larger than 45:\n{larger_list}')
    

def display_larger(list, n):
    # display_larger – should accept the 2 parameters from main.   Using a loop, the function should compare all numbers in the list of number from the user to n.   If the number is larger than n, it should be stored in a second list containing only the numbers that are greater than n.
    
    # init larger list
    larger = []
    # loop to compare each element in list with n
    for num in list:
        # if element is larger than n, add to larger list
        if num > n:
            larger.append(num)
    # return larger list
    return larger
            
def enter_num():
    # enter_num requests user input for a number and returns it. handles exceptions by forcing reentry.
    try:
        return int(input('Enter a number: '))
    except ValueError:
        print("Enter a valid integer.")
        return enter_num()
    except:
        print("Enter a valid integer.")
        return enter_num()

if __name__ == '__main__':
    main()