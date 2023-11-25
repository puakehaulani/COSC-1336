# Practice Assignment Ch. 9-2
# Still in the groups from last class (online students do remainder of assignment), using
# the dictionary application you created, add two new menu items:
#  Save the dictionary – write a function to pickle the dictionary to a file
#  Retrieve the dictionary – write a function to retrieve the pickled
# dictionary that was saved earlier
#  Put both functions in a separate module that is imported by your main
# program
# Turn in your programs/modules to the practice assignment link in
# course content.
# This program uses a dictionary to keep track of foster dogs

import pickling

# Global constants for menu choices
VIEW_ALL = 1
LOOK_UP = 2
ADD = 3
CHANGE = 4
DELETE = 5
WRITE_FILE = 6
READ_FILE = 7
QUIT = 8

DEFAULT = 'Pupper not found in this pack.'
FILENAME = 'dogfarm.dat'
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
        elif choice == WRITE_FILE:
            pickling.save_dictionary(foster_dogs, FILENAME)
        elif choice == READ_FILE:
            pickling.get_dictionary(FILENAME)

# The get_menu_choice function displays the menu and gets a validated choice from the user.
def get_menu_choice():
    print('\n===========================')
    print('Foster dogs at the Dog Farm')
    print('---------------------------')
    print('1. View all dogs')
    print('2. Look up a dog')
    print('3. Add a new dog to the pack')
    print('4. Change a dog\'s decription')
    print('5. Remove adopted dog from the Farm')
    print('6. Save foster roster to file')
    print('7. Read saved foster roster file')
    print('8. Quit the program\n')

    chosen = enter_choice()
    return chosen 

def enter_choice():
    try:
        # Get the user's choice.
        choice = int(input('Enter your choice: '))
        # Validate the choice.
        while choice < VIEW_ALL or choice > QUIT:
            choice = int(input('Enter a valid choice: '))
        # return the user's choice.
        return choice
    except ValueError:
        print("Enter a valid choice.")
        return enter_choice()
    except:
        print("Enter a valid choice.")
        return enter_choice()

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
if __name__ == '__main__':
    main()

    
