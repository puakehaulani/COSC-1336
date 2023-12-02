# Practice Assignment Ch. 10-2
# Work in groups of 2. (Online students work on your own) One person
# writes the class, one writes the program to implement the class.
# You should have 2 files:
# • One for the class
# • One for the class implementation (main program)

# Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet.
# This data should be stored as the object's attributes. Use the object's accessor methods to retrieve the pet's name, type, and age, and display this data on the screen.

import pet

# Main creates an object of the class and prompts the user to enter the name, type, and age of his or her pet
def main():
    # Get the pet data
    name = str(input('Enter your pet\'s name: '))
    type = str(input('Enter your pet\'s type: '))
    age = str(input('Enter your pet\'s age: '))
    # create instance of Pet class
    user_pet = pet.Pet(name, type, age)
    # display the data that was entered
    print('Here is what you entered:')
    print(f'Name: {user_pet.get_name()}')
    print(f'Type: {user_pet.get_animal_type()}')
    print(f'Age: {user_pet.get_age()}')

if __name__ == '__main__':
    main()