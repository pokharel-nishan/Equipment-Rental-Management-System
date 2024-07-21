# Importing necessary modules for managing inventory, transaction and carrying out operations
from read import read_inventory_file
import write 
import operations


#UI part
# Introduction and details about the shop
print("\n\t\t\t\t      Eventual Event Equipment Rental Shop \n")
print("\t\t\t\t Bagbazzar, Kathmandu  |  Phone No: 0159423569 \n")

# Welcome message
print("\n------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t  Welcome to the system Admin!")
print("------------------------------------------------------------------------------------------------------------------\n")

user_choice = 0
# The loop will run unless user enters 3
while user_choice != 3:
    # option panel to be displayed when user wants to carry out the operation in the system
    print("\n------------------------------------------------------------------------------------------------------------------")
    print("Select the options to carry out the operations in the system ")
    print("------------------------------------------------------------------------------------------------------------------")
    print(" Select a desirable option")
    print("(1)  ||  Press 1 to rent a Equipment.")
    print("(2)  ||  Press 2 to return a Equipment.")
    print("(3)  ||  Press 3 exit. \n")
    
    # exception handling when user enters a value other than integer
    try:
        user_choice = int(input("Enter an option : "))
    # block to be executed after a exception is encountered
    except ValueError:
        print("\n !!! Please enter a valid number. !!! \n")

    # block to be executed if no exception occurs
    else:
        # Executing the below block of code if user enters 1
        if user_choice == 1:
            # reading the text file and returning the contents of text file in a dictionary
            equipment_dict = read_inventory_file()
            '''
            operations carriied out for renting the equipment
            storing the returned value in different variables to carry out further operations
            '''
            rental_result = operations.rent_equipment(equipment_dict)
            if rental_result != 0:
                invoice_generation_contents, invoice_textFile_creation_details, inventory_update = rental_result
                
                invoice_details = operations.generate_invoice(invoice_generation_contents)
                # displaying the invoice 
                print(invoice_details)

                #  adding the invoice to the list that can be used to create invoice text file
                invoice_textFile_creation_details.append(invoice_details)

                # creating a invoice text file
                write.generate_invoice_textFile(invoice_textFile_creation_details)

                # inventory_update is a updated dictionary after carrying out the rental transactions
                write.write_inventory_file(inventory_update)

        # Executing the below block of code if user enters 1
        elif user_choice == 2:
            # reading the text file and returning the contents of text file in a dictionary
            equipment_dict = read_inventory_file()
            '''
            operations carriied out for returning the equipments
            storing the returned value in different variables to carry out further operations
            '''
            invoice_generation_contents, invoice_textFile_creation_details, inventory_update = operations.return_equipment(equipment_dict)
            
            invoice_details = operations.generate_invoice(invoice_generation_contents)
            # displaying the invoice 
            print(invoice_details)

            #  adding the invoice to the list that can be used to create invoice text file
            invoice_textFile_creation_details.append(invoice_details)

            # creating a invoice text file
            write.generate_invoice_textFile(invoice_textFile_creation_details)

            # inventory_update is a updated dictionary after carrying out the return transactions
            write.write_inventory_file(inventory_update)

        # Terminating the program, if user enters 3
        elif user_choice == 3:
            print("\n System Terminated!! \n")

        # Displaying a message, if user enters a numeric value other than 1, 2 and 3
        else:
            print("\n !!! Please enter a valid option. !!! \n")



