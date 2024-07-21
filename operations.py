# importing external library in order to retrieve date and time of transaction
from datetime import datetime


# display the items in the inventory
def display_inventory(equipment_dict):
    ''' Displays the details of inventory that is stored in equipment_dict in tabular form
    This function take equipment_dict as parameter and doesnot return anything.
    This function takes information in the form of equipment_dict, iterates over the dictionary, and displays the inventory details
    '''

    print("\n")
    print("-------------------------------------------------------------------------------")
    print("S.N      Equipment \t\t Brand \t\t Price\t\tQuantity")
    print("-------------------------------------------------------------------------------")

    num = 1
    # Iterating over the values in the dictionary, and then assigning the contents of values to corresponding variables
    for values in equipment_dict.values():
        equipment, brand, price, quantity= values
        formatted_price = "$" + str(price)
        # displaying the contents of inventory
        print(num, "      ", equipment, " \t\t", brand, " \t \t", formatted_price, " \t\t ", quantity)
        num += 1
    print("-------------------------------------------------------------------------------")


def generate_invoice(invoice_generation_contents):
    '''Generate an invoice after a transaction takes place
        This function take invoice_generation_contents as parameter and returns invoice
        This function takes necessary information about a transactoin through parameter and generates an invoice
    '''

    # storing the values of the 2D list that came as a parameter, and storing the values in corresponding 1D list
    transaction_status, customer_name, contact_info, equipment_list, brand_list, price_list, quantity_list, date_format, time_format, equipment_price_list, fine_list, rental_days_list, rented_days_list = invoice_generation_contents

    '''
    concatnate the string variable invoice with multiple lines of values
    company description
    '''
    invoice = ""
    # if the equipment is rented
    if transaction_status == "rented":
        invoice += "\n\n\n--------------------------------------------------------------------------------------------------\n"
        invoice += "\t\t\t        Eventual Event Equipment Rental Shop \n"
        invoice += "\t\t\t   Bagbazzar, Kathmandu  |  Phone No: 0159423569 \n"
        invoice += "--------------------------------------------------------------------------------------------------\n"

        invoice +=  "\n\t\t\t\t****************************************************\n"
        invoice += "\t\t\t\t\t\t Equipment Rented"
        invoice +=  "\n\t\t\t\t****************************************************\n"
        invoice += "\n\t\t\t\t\t\t\t\t\t\t Date: " + date_format + "\n"
        invoice += "\t\t\t\t\t\t\t\t\t\t Time: " + time_format + "\n\n"
    # if the equipment is returned
    elif transaction_status == "returned":
        invoice += "\n\n\n--------------------------------------------------------------------------------------------------------------------------\n"
        invoice += "\t\t\t\t           Eventual Event Equipment Rental Shop \n"
        invoice += "\t\t\t\t      Bagbazzar, Kathmandu  |  Phone No: 0159423569 \n"
        invoice += "--------------------------------------------------------------------------------------------------------------------------\n"

        invoice +=  "\n\t\t\t\t    ****************************************************\n"
        invoice += "\t\t\t\t\t\t     Equipment Returned"
        invoice +=  "\n\t\t\t\t    ****************************************************\n"
        invoice += "\n\t\t\t\t\t\t\t\t\t\t\t\t Date: " + date_format + "\n"
        invoice += "\t\t\t\t\t\t\t\t\t\t\t\t Time: " + time_format + "\n\n"
    
    
    invoice += "Name:              " + customer_name + "\n"
    invoice += "Contact No:        " + str(contact_info) + "\n"
    
    if transaction_status == "rented":
        invoice += "\n---------------------------------------------------------------------------------------------------\n"
        invoice += "S.N \t Equipment Name \t Brand \t    Price(per unit)    Quantity    Rental Days     Total"
        invoice += "\n---------------------------------------------------------------------------------------------------\n"
        
        # Iterating through each tems in the list
        for i in range(len(equipment_list)):
            # formatting and storing the values of list in a variable
            formatted_each_line = str((i+1)) + " \t " + equipment_list[i] + " \t  " + brand_list[i] + " \t\t $" + str(price_list[i]) + " \t\t  " + str(quantity_list[i]) + " \t\t" + str(rental_days_list[i]) + "          $" + str(equipment_price_list[i]) + "\n"

            invoice += formatted_each_line
        invoice +="\n---------------------------------------------------------------------------------------------------\n"
        '''
        calculating the price for renting the equipments and fine amount
        And using the calculated price and fine amount to calculate total amount
        '''
        total_amount = sum(equipment_price_list)
        # Total price of renting equipments without fine
        invoice += "\n\t\t\t\t\t\t\t\t Total Amount:   $" + str(total_amount)
    

    elif transaction_status == "returned":
        invoice += "\n----------------------------------------------------------------------------------------------------------------------------\n"
        invoice += "S.N \t Equipment Name \t Brand \t    Price(per unit)    Quantity    Rental Days   Rented Days   Fine Amount    Total"
        invoice += "\n----------------------------------------------------------------------------------------------------------------------------\n"
        
        # Iterating through each tems in the list
        for i in range(len(equipment_list)):
            # formatting and storing the values of list in a variable
            formatted_each_line = str((i+1)) + " \t " + equipment_list[i] + " \t  " + brand_list[i] + " \t\t $" + str(price_list[i]) + " \t\t  " + str(quantity_list[i]) + " \t\t" + str(rental_days_list[i]) + " \t\t" + str(rented_days_list[i]) + " \t   $" + str(fine_list[i]) + " \t $" + str(equipment_price_list[i]) + "\n"

            invoice += formatted_each_line
        invoice +="\n----------------------------------------------------------------------------------------------------------------------------\n"
        
        '''
        calculating the price for renting the equipments and fine amount
        And using the calculated price and fine amount to calculate total amount
        '''

        total_fine = sum(fine_list)
        total_amount= sum(equipment_price_list)
        # Total price of renting equipments without fine
        invoice += "\n\t\t\t\t\t\t\t\t\t\t\t\t Total Fine:     $" + str(total_fine)
        invoice += "\n\t\t\t\t\t\t\t\t\t\t\t\t Total Amount:   $" + str(total_amount)

        
       # returning the formatted invoice that is ready to be displayed or written in a text file
    return invoice



def rent_equipment(equipment_dict):
    ''' Rent the equipment from the inventory, and collects necessary data to create invoice and to update inventory
    This function takes equipment_dict as parameter and returns for_generating_invoice(list), generate_invoice_text_file(list), updating_inventory(dict) in the form of tuple
    This function interacts with the user to rent equipment i.e, take inputs from the user, collect enough data to generate invoice, and update the inventory
    '''

    print("\n ------------------- Rent Equipment!! -------------------- \n")
    # Asking the user to enter the name and contact number of customer
    customer_name = input("Enter Customer's name:       ")

    valid_contact_info = True
    # This loop will run until valid contact number is entered
    while valid_contact_info == True:
        # exception handling when user enters a value other than integer
        try:
            contact_info = int(input("Enter Customer's contact number:      "))
            
            '''
            ensuring the valid contact info
            First condition checks if the number is positive or not 
            Second condition checks if the length of contact number is 10 or not by converting contact number to string
            '''
            if contact_info >= 0 and len(str(contact_info)) == 10:
                # breaking out of the loop if the contact number is valid
                valid_contact_info = False
            else:
                print("\n !!! Print enter valid contact number. !!! \n")
        # block to be executed after an exception is encountered
        except:
            print("\n !!! Please enter a valid number. !!! \n") 
    
    print("\n")
    # Initializing a empty list to store the list of equipments that users want to rent at once
    equipment_list = []
    # Initializing a empty list to store the list of brands of the equipments that users want to rent
    brand_list = []
    # Initializing a empty list to store the list of price of the equipments to be rented by a user
    price_list = []
    # Initializing a empty list to store the list of quantity of equipments to be rented by a user
    quantity_list = []
    # Initializing a empty list to store the list for storing calculated prices on 5 days basis
    equipment_price_list = []
    # Initializing a empty list to store the for storing fine amount and rented days
    fine_list = []
    rented_days_list = []
    # Initializing a empty list to store the for storing rental days for each eqiupment
    rental_days_list = []
    
    continue_ = "y"
    # This loop will handle the condition if user want to rent more than one equipment
    while continue_ != "n":
        '''
        every time equipment id is not valid, the details of inventory is shown
        and the while loop will execute
        '''
        user_choice = "y"
        while True:
            # displaying the contents of inventory
            display_inventory(equipment_dict)
        # exception handling when user enters a value other than integer
            try:
                equipment_id = int(input("\nEnter the equipment that user want to rent:   "))
        
            
                '''
                check whether the equipment is available in our inventory or not
                if the equipment id is valid break the while loop and proceed forward
                '''
                if equipment_id <= len(equipment_dict) and equipment_id >=1:
                   # Check if the quantity is available in inventory
                    if equipment_dict[equipment_id][3] <= 0:
                        print("\n !!! Equipment is not available in the inventory. !!!\n")
                        while True:
                            user_choice = input("Do you want to rent other equipment? (y/n): ")
                            # Go back to selecting equipment
                            if user_choice.lower() == "y":
                                break
                            # exit this loop and continue the rental process
                            elif user_choice.lower() == "n" :
                                break
                            else:
                                print("\n !!! Please enter valid option. !!! \n")
                    # Valid equipment selected, proceed forward
                    else:
                        break
                    if user_choice == "n":
                        break
                else: 
                    print("\n !!! Please enter valid Equipment Id. !!! \n")
            
            except ValueError:
                print("\n !!! Please enter a valid number. !!! \n") 



        '''
        if the user does not want to rent other equipment
        after there is no available quantity in the inventory
        '''
        if user_choice == "n":
            print("\n !!! Rental Process Ended !!!")
            continue_ = "n"
            break
            
        # adding the names of each equipment to a list after equipmentId is valid
        equipment_name = equipment_dict[equipment_id][0]
        equipment_list.append(equipment_name)
        # adding the names of each brand of the equipment 
        brand_list.append(equipment_dict[equipment_id][1])
        # adding the price of each equipement to a list
        price_list.append(equipment_dict[equipment_id][2])
        
        '''
        substracting a quantity of partiular equipment from the dictionary after valid quantity is entered
        This loop will continue until valid quantity is entered          
        '''
        valid_quantity = True
        while valid_quantity == True:
            # exception handling when user enters a value other than integer
            try:
                quantity = int(input("Enter the number of " + equipment_name + " user want to rent:     "))
                
                # Ensuring the quantity entered by user is valid and is available
                if quantity <= 0:
                    print("\n !!! Please enter a valid number for quantity. !!! \n")
                    print("***********************************************************************************************************\n")
                    print("\t Available Quantity of ", equipment_name, " in the inventory:   ", str(equipment_dict[equipment_id][3]))
                    print("\n***********************************************************************************************************\n")
                elif quantity > equipment_dict[equipment_id][3]:
                    print("\n !!! Insufficient quantity in the inventory. !!! \n")
                    print("***********************************************************************************************************\n")
                    print("\t Available Quantity of ", equipment_name, " in the inventory:   ", str(equipment_dict[equipment_id][3]))
                    print("\n***********************************************************************************************************\n")

                    '''
                    If the quantity entered by user is valid, add the quantity to the list
                    And then deduct the quantity from the dictionary, which can later be used to update inventory
                    '''
                else:
                    quantity_list.append(quantity)
                    equipment_dict[equipment_id][3] -= quantity
                    valid_quantity = False
            # block of code to be executed after an exception is encountered
            except ValueError:
                print("\n !!! Please enter a valid number. !!! \n") 
                print("***********************************************************************************************************\n")
                print("\t Available Quantity of ", equipment_name, " in the inventory:   ", str(equipment_dict[equipment_id][3]))
                print("\n***********************************************************************************************************\n")


       
        valid_days = True
        # this loop will run until a user enters a valid days i.e days > 0
        while valid_days == True:
            # exception handling when user enters a value other than integer
            try:
                rental_days = int(input("How many days do the user want to rent the equipment:      "))
                # if the input for rental_days is less than 0
                if rental_days <= 0:
                    print("\n !!! Please enter valid days. !!! \n")
                    # the below else block of code will execute if the days entered by the user is valid
                else:
                    equipment_price = equipment_dict[equipment_id][2]
                    '''
                    The rental price is calculated per 5 days basis and stored in a variable
                    per 5 days basis: 4//5 generates 0, 6//5 generates 1 i.e closest rounds down integer
                    eg: if days = 5/4/3: price = equipment_price, if days = 6/7/8: price = equipment_price + equipment_price
                    '''
                    equipment_price_5_day = (rental_days // 5) * equipment_price
                    # if remainder is not equal to 0, add the rental price of equipment once
                    if rental_days % 5 != 0:
                        equipment_price_5_day += equipment_price
                    # calculating the price of renting the equipment for x quantity
                    equipment_total_price = equipment_price_5_day * quantity
                    # Adding the calculated price and the rental days to the list
                    equipment_price_list.append(equipment_total_price)
                    rental_days_list.append(rental_days)
                    rented_days = 0
                    rented_days_list.append(rented_days)
                    # since it is for rental, so there will be no fine for the time when renting
                    fine = 0
                    fine_list.append(fine)
                    # Message to be displayed after successfully renting the equipment
                    print("\n*******************************************")
                    print("Equipment added to the bag")
                    print("*******************************************\n")

                    valid_days = False
            # the below block of code will execute if the user inputs non numeric values 
            except:
                print("\n !!! Please enter a valid number. !!! \n") 

        
        
        
        valid_choice = True
        # This loop will run until user enters either "y" or "n"
        while valid_choice == True:
            continue_ = input("Do you wish to continue (y/n):          ")
            if continue_ == "y" or continue_ == "n":
                valid_choice = False
            else:
                print("!!! Please enter correct option. !!!")

    # Retrieving the date and time of transaction
    equipment_rental_date_time = datetime.now()
    # formatting the date and time for later use
    date_format = equipment_rental_date_time.strftime("%Y-%m-%d")
    time_format = equipment_rental_date_time.strftime("%H:%M:%S")


    # if there is equipment in the list, then only the following actions will take place
    if len(equipment_list) != 0: 
        transaction_status = "rented"

        # list of items that are needed to generate invoice
        for_generating_invoice = [transaction_status, customer_name, contact_info, equipment_list, brand_list, price_list, quantity_list, date_format, time_format, equipment_price_list, fine_list, rental_days_list, rented_days_list ]
    
        # list of items that are needed to generate invoice text file
        generate_invoice_textFile = [transaction_status, customer_name, equipment_rental_date_time]

        # updated dictionary which is needed to update the quantities in the inventory file
        updating_inventory = equipment_dict

        # returning the details needed to generate invoice, generate invoice text file and update inventory file
        return for_generating_invoice, generate_invoice_textFile, updating_inventory
    # Following message will display if the list of equipment is empty
    else:
        print("!!! Transaction cannot be completed. Please try again. !!!")
        return 0




def return_equipment(equipment_dict):
    ''' Return the equipment to the inventory, and collects necessary data to create invoice and to update inventory
    This function takes equipment_dict as parameter and returns for_generating_invoice(list), generate_invoice_text_file(list), updating_inventory(dict) in the form of tuple
    This function interacts with the user to return equipment i.e, take inputs from the user, collect enough data to generate invoice, and update the inventory
    '''

    print("\n ------------------- Return Equipment!! -------------------- \n")
    # Asking the user to enter the name of customer
    customer_name = input("Enter Customer's name:       ")

    valid_contact_info = True
    # This loop will run until valid contact number is entered
    while valid_contact_info == True:
        # exception handling when user enters a value other than integer
        try:
            contact_info = int(input("Enter Customer's contact number:      "))
            
            '''
            ensuring the valid contact info
            First condition checks if the number is positive or not 
            Second condition checks if the length of contact number is 10 or not by converting contact number to string
            '''
            if contact_info >= 0 and len(str(contact_info)) == 10:
                # breaking out of the loop if the contact number is valid
                valid_contact_info = False
            else:
                print("\n !!! Print enter valid contact number. !!! \n")
        # block to be executed after an exception is encountered
        except:
            print("\n !!! Please enter a valid number. !!! \n") 


    print("\n")
    # Initializing a empty list to store the list of equipments that users want to return at once
    equipment_list = []
    # Initializing a empty list to store the list of brands of the equipments that users want to return
    brand_list = []
    # Initializing a empty list to store the list of price of the equipments to be returned by a user
    price_list = []
    # Initializing a empty list to store the list of quantity of equipments to be returned by a user
    quantity_list = []
    # Initializing a empty list to store the list for storing calculated prices on 5 days basis
    equipment_price_list = []
    # Initializing a empty list to store the for storing fine amount
    fine_list = []
    # Initializing a empty list to store the for storing rental days for each eqiupment
    rental_days_list = []
    # Initializing a empty list to store the for storing rented days for each eqiupment
    rented_days_list = []
    
    continue_ = "y"
    # This loop will handle the condition if user want to return more than one equipment
    while continue_ != "n":  
        '''
        every time equipment id is not valid, the details of inventory is shown
        and the while loop will execute
        '''
        while True:
            # displaying the contents of inventory
            display_inventory(equipment_dict)
            # exception handling when user enters a value other than integer
            try:
                equipment_choice = int(input("\nEnter the equipment that user want to return:   "))
                
                '''
                check whether the equipment is available in our inventory or not
                if the equipment id is valid break the while loop and proceed forward
                '''
                if equipment_choice <= len(equipment_dict) and equipment_choice >=1:
                    break
                else: 
                    print("\n !!! Please enter valid Equipment Id. !!! \n")
            # block to be executed after an exception is encountered
            except ValueError:
                print("\n !!! Please enter a valid number. !!! \n") 
            
        # adding the names of each equipment to a list after equipmentId is validated
        equipment_name = equipment_dict[equipment_choice][0]
        equipment_list.append(equipment_name)
        # adding the names of each brand of the equipment 
        brand_list.append(equipment_dict[equipment_choice][1])
        # adding the price of each equipement to a list
        price_list.append(equipment_dict[equipment_choice][2])

        '''
        adding a quantity of particular equipment to the dictionary after valid quantity is entered
        This loop will continue until valid quantity is entered          
        '''             
        valid_quantity = True
        while valid_quantity == True:
            # exception handling when user enters a value other than integer
            try:
                quantity = int(input("Enter the number of " + equipment_name + " user want to return:     "))
                
                # ensuring the quantity entered by the user is valid
                if quantity <= 0:
                    print("\n !!! Please enter a valid number for quantity. !!! \n")
                    
                    '''
                    If the quantity entered by user is valid, add the quantity to the list
                    And then add the quantity to the dictionary, which can later be used to update inventory
                    '''
                else:
                    quantity_list.append(quantity)
                    equipment_dict[equipment_choice][3] += quantity
                    valid_quantity = False
            # block to be executed after an exception is encountered
            except ValueError:
                print("\n !!! Please enter a valid number. !!! \n") 


        valid_rental_days = True
        # This loop will run until valid rental days is entered
        while valid_rental_days == True:
            # exception handling when user enters a value other than integer
            try:
                rental_days = int(input("How many days did the user take the equipment for rental:   "))
                
                # ensuring the valid rental days
                if rental_days <= 0:
                    print("\n !!! Print enter valid days. !!! \n")
                else:
                    # breaking out of the loop if the rental_days is valid
                    valid_rental_days = False
            # block to be executed after an exception is encountered
            except:
                print("\n !!! Please enter a valid number. !!! \n") 


        valid_rented_days = True
        # This loop will run until valid rented days is entered
        while valid_rented_days == True:
            # exception handling when user enters a value other than integer
            try:
                rented_days = int(input("How many days did the user rented the equipment:      "))
                
                # ensuring the valid rented days
                if rented_days <= 0:
                    print("\n !!! Print enter valid days. !!! \n")
                # breaking out of the loop if the rented_days is valid
                else:
                    rented_days_list.append(rented_days)
                    valid_rented_days = False
            # block to be executed after an exception is encountered
            except:
                print("\n !!! Please enter a valid number. !!! \n") 
        
        equipment_price = equipment_dict[equipment_choice][2]
        '''
        if both rented_days and rental_days have valid inputs
        proceed to calculate the fine amount, total amount and so on
        '''
        if rented_days >= 0 and rental_days >= 0:
            
            fine_amount = 0
            # price per day is calculated to apply fine on per day basis
            price_per_day = equipment_price / 5
            '''
            The rental price is calculated per 5 days basis and stored in a variable
            per 5 days basis: 4//5 generates 0, 6//5 generates 1 i.e closest rounds down integer
            eg: if days = 5/4/3: price = equipment_price, if days = 6/7/8: price = equipment_price + equipment_price
            '''
            equipment_price_5_day = (rental_days // 5) * equipment_price
            # if remainder is not equal to 0, add the rental price of equipment once
            if rental_days % 5 != 0:
                equipment_price_5_day += equipment_price
            
             # if rental days is not divisible by 5 (because of 5 days basis)
            if rental_days % 5 != 0:
                '''
                the user always pays the rental charge on the basis of 5 days
                if the user rents for 7 days, he will pay the charge of 10 days
                so here we are rounding up the the number to upper number divisible by 5
                '''
                rental_days = ((rental_days//5) +1) * 5 
            # calculating the days difference to calculate fine amount if applicable
            '''
            if the user rented the equipment for more than mentioned rental rate
            then only the fine will be calculated and added total
            '''
            if rented_days > rental_days:
                days_difference = rented_days - rental_days
                '''
                if user rented for 3 days and returned the item in 4 days, a negative value will occur
                because the 3 will round up to 5 days while paying the rental, and  4 - 5 = -1
                so to prevent that error, we have applied the condition if only days difference > 0
                '''
                if days_difference > 0:
                    fine_amount = days_difference * price_per_day * quantity
                # if there is no days difference or if the day difference is < 0, assign 0 to fine amount
                else:
                    fine_amount = 0

            # calculating the total price of renting the equipment including the fine the fine
            equipment_total_price = equipment_price_5_day * quantity + fine_amount

            # adding the calculated price to the list
            equipment_price_list.append(int(equipment_total_price))

            # adding the fine amount to the list
            fine_list.append(int(fine_amount))
            # adding the rental days to the list
            rental_days_list.append(rental_days)
        # Message to be displayed after successfully returning the equipment 
        print("\n*******************************************")
        print("Equipment added to the inventory")
        print("*******************************************\n")

                    
        valid_choice = True
        # This loop will run until user enters either "y" or "n"
        while valid_choice == True:
            continue_ = input("Do you wish to continue (y/n):          ")
            if continue_ == "y" or continue_ == "n":
                valid_choice = False
            else:
                print("!!! Please enter correct option. !!!")
            
    # retrieving the date and time of transaction
    equipment_return_date_time = datetime.now()
    # formatting the date and time for later use
    date_format = equipment_return_date_time.strftime("%Y-%m-%d")
    time_format = equipment_return_date_time.strftime("%H:%M:%S")


    # if there is equipment in the list, then only the below actions will take place
    if len(equipment_list) != 0: 
        transaction_status = "returned"

        # list of items that are needed to generate invoice
        for_generating_invoice = [transaction_status, customer_name, contact_info, equipment_list, brand_list, price_list, quantity_list, date_format, time_format, equipment_price_list, fine_list, rental_days_list, rented_days_list]

        # list of items that are needed to generate invoice text file
        generate_invoice_textFile = [transaction_status, customer_name, equipment_return_date_time]

        # updated dictionary which is needed to update the quantities in the inventory file
        updating_inventory = equipment_dict 

        # returning the details needed to generate invoice, generate invoice text file and update inventory file
        return for_generating_invoice, generate_invoice_textFile, updating_inventory
    # Following message will display if the list of equipment is empty
    else:
        print("!!! Transaction cannot be completed. Please try again. !!!")


