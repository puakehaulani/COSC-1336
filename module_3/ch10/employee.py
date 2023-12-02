# Personal Information Class:   
# Design a class called Employee that holds the following data about an employee: 
# name 
# ID number 
# Department 
# Job Title 

# Class.   Store your class in a separate file called employee.py. 
# Your class will have an initializer method that will be passed the information entered by the user as arguments.   
# Write appropriate accessor and mutator methods for each data attribute.    
# Write a __str__ method to print the contents of the class (see example of __str__ on p. 523). 

class Employee:
    # initializer method
    def __init__(self, name, id, dept, job_title):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__job_title = job_title
    
     # The set_name method accepts an argument for the employee's name
    def set_name(self, name):
        self.__name = name 

    # The set_id method accepts an argument for the employee's id
    def set_id(self, id):
        self.__id = id 
        
    # The set_dept method accepts an argument for the employee's dept
    def set_dept(self, dept):
        self.__dept = dept
        
    # The set_job_title method accepts an argument for the employee's job_title
    def set_job_title(self, job_title):
        self.__job_title = job_title
        
    # The get_name method returns the employee's name
    def get_name(self):
        return self.__name

    # The get_id method returns the employee's id
    def get_id(self):
        return self.__id
    
    # The get_dept method returns the employee's dept
    def get_dept(self):
        return self.__dept
    
    # The get_job_title method returns the employee's job_title
    def get_job_title(self):
        return self.__job_title
    
    # __str__ method
    def __str__(self):
        return f'Name: {self.__name}\nID number: {self.__id}\nDepartment: {self.__dept}\nTitle: {self.__job_title}'
