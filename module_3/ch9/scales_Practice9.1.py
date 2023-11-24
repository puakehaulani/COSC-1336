# Practice Assignment Ch. 9-1
# 1. Classroom Sections: Group assignment – break into groups of 3 or 4.
# 2. Online students: do on your own.
# 3. Using the example of the birthday dictionary in Chapter 9, create a dictionary application, subject of your choosing
# (appropriate content)
# 4. In addition to the menu choices provided to the user in the example, add menu items to display the entire
# dictionary.
# 5. Each person will create a separate module for their function(s) with the main program importing all the modules.
#  Person 1 – main program/menu display, coordinates other programs
#  Person 2 – Look up and display functions
#  Person 3 – Add function
#  Person 4 - Change, and Delete functions
# Turn in your programs/modules to the practice assignment link in course content.


# This program uses a dictionary to keep track of foster dogs

# Global constants for menu choices
VIEW_ALL = 1
LOOK_UP = 2
ADD = 3
CHANGE = 4
DELETE = 5
QUIT = 6

DEFAULT = 'Pupper not found in this pack.'
# main function
def main():
    # Create an empty dictionary.
    foster_dogs = {}

    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == VIEW_ALL:
            view_dogs(foster_dogs)
        elif choice == LOOK_UP:
            look_up(foster_dogs)
        elif choice == ADD:
            add(foster_dogs)
        elif choice == CHANGE:
            change(foster_dogs)
        elif choice == DELETE:
            delete(foster_dogs)

# The get_menu_choice function displays the menu and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('===========================')
    print('Foster dogs at the Dog Farm')
    print('---------------------------')
    print('1. View all dogs')
    print('2. Look up a dog')
    print('3. Add a new dog to the pack')
    print('4. Change a dog\'s decription')
    print('5. Remove adopted dog from the Farm')
    print('6. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < VIEW_ALL or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The view_dogs function displays all the dogs and descriptions in the foster_dogs dictionary in a readable format.
def view_dogs(foster_dogs):
    if len(foster_dogs) == 0:
        print('No dogs on the farm right now')
    else:
        print('----------------------')
        print('Name\tDescription')
        print('----------------------')
        
        for dog in foster_dogs:
            print(f'{dog}\t{foster_dogs[dog]}')
    
# The look_up function looks up a name in the foster_dogs dictionary.
def look_up(foster_dogs):
    # Get a name to look up.
    name = input('Enter a dog\'s name: ').lower()

    # Look it up in the dictionary.
    description = foster_dogs.get(name, DEFAULT)
    if description is not DEFAULT:
        print(f'{name.capitalize()}\'s description: {description}')
    else:
        print(DEFAULT)

# The add function adds a new entry into the foster_dogs dictionary.
def add(foster_dogs):
    # Get a name and description.
    name = input('Enter the dog\'s name: ').lower()
    description = input('Enter a word to describe the dog: ')

    # If the name does not exist, add it.
    if name not in foster_dogs:
        foster_dogs[name] = description
    else:
        print(f'A profile for {name.capitalize()} already exists.\n')

# The change function changes an existing entry in the foster_dogs dictionary.
def change(foster_dogs):
    # Get a name to look up.
    name = input('Enter the dog\'s name: ').lower()

    if name in foster_dogs:
        # Get a new description.
        description = input('Enter a new description word: ')

        # Update the entry.
        foster_dogs[name] = description
    else:
        print(f'{DEFAULT}\n')
        
# The delete function deletes an entry from the foster_dogs dictionary when a dog is adopted.
def delete(foster_dogs):
    # Get a name to look up.
    name = input('Enter the dog\'s name: ').lower()

    # If the name is found, delete the entry.
    if name in foster_dogs:
        del foster_dogs[name]
        print(f'Congrats on finding {name.capitalize()} their furever home!\n')
    else:
        print(F'{DEFAULT}\n')

# Call the main function.
main()

    
