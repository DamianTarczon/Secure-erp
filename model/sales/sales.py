""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def list_transactions():
    list_of_transactions = []
    table = data_manager.read_table_from_file(DATAFILE)
    content = [word.split(";") for word in table.readlines()]
    for i in content:
        list_of_transactions.append(i[1])
    print("This is a list of transactions!")
    return list_of_transactions

def add_transaction(table):
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    customer = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    product = input("Name of product: ")
    price = input("Price of product: ")
    year = input("Year of transaction: ")
    month = input("Month of transaction: ")
    day = input("Day of transaction: ")
    date = f'{year}-{month}-{day}'
    record = [id, customer, product, price, date]
    table.append(record)
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    print("New  customer has been added!") 
    return table

def update_transaction():
    id_index = 0
    customer_index = 1
    product_index = 2
    price_index = 3
    date_index = 4
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    transaction_to_update = input("Please provide id number of transaction you want to update: ")
    for line in table:
        if line[id_index] == transaction_to_update:
            print(f"You choose {line[customer_index]} to update!")
            update = input(f"Please provide category to update for {id_index} (id, customer, product, price, date): ")
            if update == "id".lower():
                line[id_index] = id
                print(f"Id for {line[id_index]} has been changed!")
            elif update == "customer".lower():
                old_name = line[customer_index]
                line[customer_index] = id
                print(f"Customer for {old_name} has been changed! Now {old_name}'s name is {id}.")
            elif update == "product".lower():
                line[product_index] = input(f"Please provide new product name for {line[product_index]}: ")
                print(f"Product name for {line[id_index]} has been changed!")
            elif update == "price".lower():
                line[price_index] = input(f"Please provide new price for {line[id_index]}: ")
                print(f"Price for {line[id_index]} has been changed!")
            elif update == "date".lower():
                year = input("Enter year: ")
                month = input("Enter month: ")
                day = input("Enter day: ")
                line[date_index] = f'{year}-{month}-{day}'
                print(f"Date for {line[id_index]} has been changed ")
        else:
            print(f"There isn't id like {transaction_to_update} in file! Please choose correct customer.")
            return update_transaction(table) 
    data_manager.write_table_to_file(DATAFILE, table, separator=';') 
    return table

def delete_transaction(table):
    id_index = 0
    table = data_manager.read_table_from_file(DATAFILE)
    customer_to_delete = input("Please provide id number of transaction you want to remove: ")
    for line in table:
        if line[id_index] == customer_to_delete:
            table.remove(line)
            print(f"Transaction with id number {customer_to_delete} has been removed!")
        else:
            print(f"There isn't id number like {customer_to_delete} in file! Please choose correct transaction.")
            return delete_transaction(table)
    data_manager.write_table_to_file(DATAFILE, table, separator=';') 
    return table

def get_biggest_revenue_transaction():
    transaction_list = data_manager.read_table_from_file(DATAFILE)
    transaction_id = ['not_given']
    id_index = 0
    value_index = 3
    max_value = 0
    for line in transaction_list:
        line = re.split(r';',line)
        if float(line[value_index]) > max_value:
            transaction_id[id_index] = line[id_index]
            max_value = float(line[value_index])
    return transaction_id[id_index]

def get_biggest_revenue_product():
    

    pass

def count_transactions_between():
    id = []
    customer = []
    product = []
    price = []
    date = []
    file = data_manager.read_table_from_file(DATAFILE)
    for line in file:
        all_lists = line.split(";")
        id.append(all_lists[0])
        customer.append(all_lists[1])
        product.append(all_lists[2])
        price.append(all_lists[3])
        date.append(all_lists[4])
    new_dict = {}
    new_dict[HEADERS[0]] = id
    new_dict[HEADERS[1]] = customer
    new_dict[HEADERS[2]] = product
    new_dict[HEADERS[3]] = price
    new_dict[HEADERS[4]] = date
    year1 = input("Enter starting year: ")
    month1 = input("Enter starting month: ")
    day1 = input("Enter starting day: ")
    year2 = input("Enter ending year: ")
    month2 = input("Enter ending month: ")
    day2 = input("Enter ending day: ")
    data_from_file = pd.DataFrame(new_dict)
    start_date = f'{year1}-{month1}-{day1}'
    end_date = f'{year2}-{month2}-{day2}'
    mask = (data_from_file['Date'] > start_date) & (data_from_file['Date'] <= end_date)
    data_from_file = data_from_file.loc[mask]
    return len(data_from_file)


def sum_transactions_between():
    id = []
    customer = []
    product = []
    price = []
    date = []
    file = data_manager.read_table_from_file(DATAFILE)
    for line in file:
        all_lists = line.split(";")
        id.append(all_lists[0])
        customer.append(all_lists[1])
        product.append(all_lists[2])
        price.append(all_lists[3])
        date.append(all_lists[4])
    new_dict = {}
    new_dict[HEADERS[0]] = id
    new_dict[HEADERS[1]] = customer
    new_dict[HEADERS[2]] = product
    new_dict[HEADERS[3]] = price
    new_dict[HEADERS[4]] = date
    year1 = input("Enter starting year: ")
    month1 = input("Enter starting month: ")
    day1 = input("Enter starting day: ")
    year2 = input("Enter ending year: ")
    month2 = input("Enter ending month: ")
    day2 = input("Enter ending day: ")
    data_from_file = pd.DataFrame(new_dict)
    start_date = f'{year1}-{month1}-{day1}'
    end_date = f'{year2}-{month2}-{day2}'
    mask = (data_from_file['Date'] > start_date) & (data_from_file['Date'] <= end_date)
    data_from_file = data_from_file.loc[mask]
    data_from_file['Price'] = data_from_file['Price'].astype(float)
    total = data_from_file['Price'].sum()
    return total 

    


