from model.sales import sales
from view import terminal as view

HEADERS = ["Id", "Customer", "Product", "Price", "Date"]

def list_transactions():
    view.print_table(sales.list_transactions(), HEADERS)
    # view.print_error_message("Not implemented yet.")


def add_transaction():  
    sales.add_transaction()
    # view.print_error_message("Not implemented yet.")


def update_transaction():
    view.print_table(sales.update_transaction(), HEADERS)
    # view.print_error_message("Not implemented yet.")


def delete_transaction():
    sales.delete_transaction()
    # view.print_error_message("Not implemented yet.")


def get_biggest_revenue_transaction():
    transaction = sales.get_biggest_revenue_transaction()
    print(f"ID of transaction that brought biggest revenue is: {transaction}")
    # view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    product = sales.get_biggest_revenue_product()
    print(f"{product} is product which brought biggest revenue")
    # view.print_error_message("Not implemented yet.")


def count_transactions_between():
    count = sales.count_transactions_between()
    print(f"Count transaction between given dates is {count}")
    # view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    transaction_sum = sales.sum_transactions_between()
    print(f" Sum transaction between given dates is {transaction_sum}")
    # view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)

