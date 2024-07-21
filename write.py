
# updating the contents of dictionary after the transactions are carried out
def write_inventory_file(equipment_dict):
    '''Updating the inventory text file after a transaction takes place
    This function takes equipment_dict as a parameter and does not return anything
    After taking the dictinary as a parameter, this assigns the values inside the dictionary to corresponding variables
    - and writes the changes back into the file using those variables
    '''
    
    file_lines = ""
    # Iterating over the values of equipment_dict, assigning each value in the list to corresponding variable
    for values in equipment_dict.values():
        name = values[0]
        brand = values[1]
        price = values[2]
        quantity = values[3]
        formatted_price = "$" + str(price)
        formatted_quantity = str(quantity)
        each_line = name + ", " + brand + ", " + formatted_price + ", " + formatted_quantity + " \n"
        file_lines += each_line
    # opening the inventory file in write mode to update the inventory text file
    with open("inventory.txt", "w") as file:
        # updating the inventory after making the transactions
        file.write(file_lines)
        print("\n********************************************")
        print( "!!!Inventory Updated!!!")
        print("********************************************\n")

def generate_invoice_textFile(invoice_creation_textFile_details):
    '''Generate unique text file for each transaction's invoice
    Takes a invoice_creation_textFile_details(list) as a parameter and does not return anything
    This function generates a seperate text files for rental and returned invoices, using the details inside the list invoice_creation_textFile_details that came as parameter
    '''
    transaction_status, customer_name, transaction_date_time, invoice_details = invoice_creation_textFile_details
     # using the return date time of equipment to make unique filename
    date_time = transaction_date_time.strftime('%Y%m%d%H%M%S')

    # generating the rented invoice text file
    if transaction_status == "rented":
        unique_file_name = date_time + "_" + customer_name + "_" + "rental_invoice.txt" 
        with open(unique_file_name, "w") as file:
            # writing the contents of invoice in a uniquely named text_file
            file.write(invoice_details)
            print( "\n********************************************")
            print("!!!Rental Invoice Generated!!!")
            print( "********************************************\n")

    # generating the returned invoice text file
    elif transaction_status == "returned":
        unique_file_name = date_time + "_" + customer_name + "_" + "return_invoice.txt" 
         # creating a new file with unique_file_name in write mode
        with open(unique_file_name, "w") as file:
            # writing the contents of invoice in a uniquely named text_file
            file.write(invoice_details)
            print( "\n********************************************")
            print("!!!Returned Invoice Generated!!!")
            print( "********************************************\n")

