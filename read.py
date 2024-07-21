def read_inventory_file():
    '''Read the contents of inventory text file 
    This function does not take any parameter and returns dictionary
    This function reads the inventory text file line by line and converts the data into a dictionary
    '''
    # dictionary to store the data after reading the file
    equipments_dictionary= {}
    counter = 1
    
    # opening the inventory file in read mode
    with open("inventory.txt", "r") as file:
        # read the file line by line 
        for each_line in file:
            '''
            stripping the whitespaces from the starting and ending of each line
            And, splitting each string in the line by comma, and storing then in corresponding variables
            '''
            name, brand, price, quantity= each_line.strip().split(", ")
            #striping and type casting: striping $ sign from the string then converting the string to integer
            price = int(price.strip("$"))
            #type casting: converting string quantity in the text file to integer
            quantity = int(quantity)
            # creating a list that stores all the equipment information
            equipment_info = [name, brand, price, quantity]
            #creating a dictionary  with 1,2,3 as key and equipment_info list as value in a list
            equipments_dictionary[counter] = equipment_info
            counter += 1
            # returning a dictionary that contains unique values as key and name, brand, price and quantity in list as values
    return equipments_dictionary
