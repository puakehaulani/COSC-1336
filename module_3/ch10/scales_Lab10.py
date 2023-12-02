# lexi scales, complete
# this program creates three instances of the employee class. it returns the information to the user.
import employee

# Your main program should create three instances of the class.   Your program should get the information from the user and pass it as parameters to the initializer method.    Using the __str__ method invoked by the print function, the program should display the personal information for the three individuals. 
def main():
    # Get user input for first employee
    name1 = str(input('Enter employee name: '))
    id1 = str(input('Enter employee ID: '))
    dept1 = str(input('Enter department: '))
    title1 = str(input('Enter position: '))
    print()
    # Get user input for second employee
    name2 = str(input('Enter employee name: '))
    id2 = str(input('Enter employee ID: '))
    dept2 = str(input('Enter department: '))
    title2 = str(input('Enter position: '))
    print()
    # Get user input for third employee
    name3 = str(input('Enter employee name: '))
    id3 = str(input('Enter employee ID: '))
    dept3 = str(input('Enter department: '))
    title3 = str(input('Enter position: '))
    print()
    # Create three employee instances
    employee1 = employee.Employee(name1, id1, dept1, title1)
    employee2 = employee.Employee(name2, id2, dept2, title2)
    employee3 = employee.Employee(name3, id3, dept3, title3)
    
    print('Employee 1:')
    print(employee1)
    print('Employee 2:')
    print(employee2)
    print('Employee 3:')
    print(employee3)


if __name__== '__main__':
    main()