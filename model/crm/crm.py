""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util
import common 

DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


# def start_module_crm():
#     while True:
#         ui.print_menu(title, option)
#         try:
#             run_operation(options)
#         except ValueError:
#             break
#         except KeyError:
#             ui.print_error_message(message)


def list_customers(table):
    list_of_customers = []
    table = data_manager.read_table_from_file(DATAFILE)
    content = [word.split(";") for word in table.readlines()]
    for i in content:
        list_of_customers.append(i[1])
    print("This is a list of our customers!")
    return list_of_customers


def add_customer(table):
    table = data_manager.read_table_from_file(DATAFILE)
    id = common.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    name = input("Enter new customer's username: ")
    email = input(f"For {name} enter email address: ")
    sub = input(f"Is {name} subscribed to the newsletter? (1: yes, 0: no): ")
    record = [id, name, email, sub]
    table.append(record)
    data_manager.write_table_to_file(DATAFILE, table, separator=';')
    print(f"New customer {name} has been added!") 
    return table


def update_customer(table):
    table = data_manager.read_table_from_file(DATAFILE)
    id = common.generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!")
    customer_to_update = input("Please provide name of customer you want to update: ")
    for line in table:
        if line[1] == customer_to_update:
            print(f"You choose {line[1]} to update!")
            update = input(f"Please provide category to update for {line[1]} (id, name, email, sub): ")
            if update == "id".lower():
                line[0] = id
                print(f"Id for {line[1]} has been changed!")
            elif update == "name".lower():
                old_name = line[1]
                new_name = input(f"Please provide new name for {old_name}: ")
                line[1] = new_name 
                print(f"Name for {old_name} has been changed! Now {old_name}'s name is {new_name}.")
            elif update == "email".lower():
                line[2] = input(f"Please provide new email for {line[1]}: ")
                print(f"Email adress for {line[1]} has been changed!")
            elif update == "sub".lower():
                line[3] = input(f"Please provide new sub-value for {line[1]}: ")
                print(f"Subscription value for {line[1]} has been changed!")
        else:
            print(f"There isn't name like {customer_to_update} in file! Please choose correct customer.")
            return update_customer(table) 
    data_manager.write_table_to_file(DATAFILE, table, separator=';') 
    return table

        
def delete_customer(table):
    table = data_manager.read_table_from_file(DATAFILE)
    customer_to_delete = input("Please provide name of customer you want to remove: ")
    for line in table:
        if line[1] == customer_to_delete:
            table.remove(line)
            print(f"Customer named {customer_to_delete} has been removed!")
        else:
            print(f"There isn't name like {customer_to_delete} in file! Please choose correct customer.")
            return delete_customer(table)  
    data_manager.write_table_to_file(DATAFILE, table, separator=';') 
    return table


def get_subscribed_emails(table):
    email_index = 2
    sub_index = 3
    list_subscribed_emails = []
    table = data_manager.read_table_from_file(DATAFILE)
    for line in table:
        if line[sub_index] == "1":
            sub_email = str(line[email_index])
            list_subscribed_emails.append(sub_email)
    print(f"This is a list of emails that subscribe to us!")
    return list_subscribed_emails