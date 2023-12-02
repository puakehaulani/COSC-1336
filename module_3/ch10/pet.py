# 1. Pet Class
# Write a class named Pet, which should have the following data attributes:
# • __name (for the name of a pet)
# • __animal_type (for the type of animal that a pet is. Example values are 'Dog', 'Cat', and 'Bird')
# • __age (for the pet's age)

# The Pet class should have an __init__ method that creates these atrributes. It should also have the following methods:
# • set_name
#   This method assigns a value to the __name field
# • set_animal_type
#   This method assigns a value to the __animal_type field
# • set_age
#   This method assigns a value to the __age field
# • get_name
#   This method returns the value of the __name field
# • get_animal_type
#   This method returns the value of the __animal_type field
# • get_age
#   This method returns the value of the __age field

class Pet:
    # The init method initializes the attributes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    # The set_name method accepts an argument for the pet's name
    def set_name(self, name):
        self.__name = name 

    # The set_animal_type method accepts an argument for the pet's animal_type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type 
        
    # The set_age method accepts an argument for the pet's age
    def set_age(self, age):
        self.__age = age
        
    # The get_name method returns the pet's name
    def get_name(self):
        return self.__name

    # The get_animal_type method returns the pet's animal_type
    def get_animal_type(self):
        return self.__animal_type
    
    # The get_age method returns the pet's age
    def get_age(self):
        return self.__age