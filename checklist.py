checklist = list() #creates a list object in memory that we can refer back to
import os # to utilize os.system('clear') to clear terminal after user input

# Remaining Tasks
# Add read, update, and destroy options to select function.
# Allow for user to use upper or lower case for function selection
# handle errors caused by invalid user input (invalid indexes)

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    print(checklist[index])

# UPDATE    
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# list all the items in list
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item)) ## format method takes arguments and places them in the curly brackets
        index += 1

def mark_completed(index):
# Add code here that marks an item as completed
  checklist[index] = ("{}:{}".format("√", checklist[index]))
  list_all_items()

# allows user to determine which functions to run (C, R, list all, list all)
def select(function_code):
    # create item, convert to lower to account for edge case with user input
    if function_code.lower() == "c": 
        input_item = user_input("Input item: ")
        create(input_item)
        os.system('clear') 
        return True
    # read item
    elif function_code.lower()  == "r":
        index_exist = True

        # evaluates if use inputted index within current checklist length
        while (index_exist == True):
            item_index = int(user_input('Index number: '))
            if item_index not in range(0, len(checklist)):
                print("Item does not exist within checklist, please try again.")
            else:
                read(item_index)
                index_exist = False
        return True
    # print all items
    elif function_code.lower()  == "p":
        list_all_items()
        return True
    # exist from loop
    elif function_code.lower()  == "q":
        os.system('clear') 
        return False
    # update item from list
    elif function_code.lower() == "u":
        input_index = int(user_input("What index would like to update? "))
        input_item = user_input("What would you like to change it to? ")
        update(input_index, input_item)
        os.system('clear') 
        return True
    # remove item from list
    elif function_code.lower() == "d":
        input_index = int(user_input("Which element would you like to delete? "))
        destroy(input_index)
        os.system('clear') 
        return True
    # mark items as completed
    elif function_code.lower() == "m":
        input_selection = int(user_input("Which item would element would you like to mark completed? "))
        mark_completed(input_selection)
        return True
    #catch all 
    else:
        print("Unknown Option")
        return True

# prompt user input
# dedicated prompt function allows us to troubleshoot if anything goes wrong
def user_input(prompt):
    user_input = input(prompt)
    return user_input


running = True
while running:
    if len(checklist) == 0:
        selection = user_input("Current list is empty. Press C to add an item to the list to begin: ")
        running = select(selection)
    else:
        selection = user_input("Checklist Options:\nC to add to list. U to update an item from list. R to read from list.\nM to mark as completed. D to delete from list. P to display list. Q to quit.\nInput Selection Here:  ")
        running = select(selection)
    



# TEST
def test():
    # creates new elements in checklist array
    create('green pants')
    create('red cloak')

    # prints the elements in inputted indices 
    print(read(0))
    print(read(1))

    # updates checklist array at provided index with provided item
    update(0, 'purple socks')
    # removes item at provided index
    destroy(1)

    print(read(0))
    list_all_items()

    # function code C to create 
    select("P")
    list_all_items()
    # function code R to read
    select("R")
    list_all_items()


# test()
# list_all_items()