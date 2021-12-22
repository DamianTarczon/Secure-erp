""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""
from datetime import date, timedelta
from model import data_manager, util
# import csv


DATAFILE = "model/hr/hr.csv"
# DATAFILE = 'C:/1Code/Projects/secure-erp-python-mateuszski/model/hr/hr.csv'
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]
table = data_manager.write_table_to_file
id_index = table[0]
name_index = table[1]
year_index = table[2]

def list_employees():
    # with open(DATAFILE, newline='') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=';')
    #     for row in reader:
    #         # print(row)
    #         return row
    table = data_manager.read_table_from_file(DATAFILE)
    return table, HEADERS


def add_employee():
    table = data_manager.read_table_from_file(DATAFILE)
    id = util.generate_id
    record = [id, input("Name: "), input("Your birth date: ")]
    table.append(record)
    data_manager.write_table_to_file(DATAFILE, table)


def update_employee():
    pass

def delete_employee():
    user_input = input("Type line number: ")
    for user_input in range(len(table)):
        if user_input == id_index:



def get_oldest_and_youngest():
    youngest_person_touple = ()
    oldest_person_touple = ()
    name_and_year_dict = {line[name_index]: line[year_index] for line in table}
    for key, value in name_and_year_dict.items():
        if value == min(name_and_year_dict.values()):
            youngest_person_touple.append(key)
            return youngest_person_touple
        elif value == max(name_and_year_dict.values()):
            oldest_person_touple.append(key)
            return oldest_person_touple

def count_employees_per_department():
    list_of_departments = []
    deparments_index = 3
    list = data_manager.read_table_from_file('hr.csv')
    dictionary_of_deparments = {}
    for i in list:
        if i[deparments_index] in list_of_departments:
            pass
        else:
            list_of_departments.append(i[deparments_index])
    for i in list_of_departments:
        count = 0
        for j in list:
            if i in j:
                count += 1
        dictionary_of_deparments[i] = count
    return dictionary_of_deparments

def count_employees_with_clearance():
    clearance_index = 4
    list = data_manager.read_table_from_file('hr.csv')
    count_employees = 0
    for i in list:
        if i[clearance_index] != '':
            count_employees += 1
    return count_employees

def next_birthdays():
    input_date = input('Write a date year/month/day: ').split('/')
    print(input_date)
    start_date = date(int(input_date[0]), int(input_date[1]), int(input_date[2]))
    days = timedelta(14)
    two_weeks_ahead_data = start_date + days
    print(two_weeks_ahead_data)
    delta = two_weeks_ahead_data - start_date
    print(delta)
    list_of_days = []
    employees_names = []
    birthday_index = 2
    name_index = 1
    for i in range(delta.days+1):
        day = start_date + timedelta(days = i)
        list_of_days.append(day)
    print(list_of_days)
    list_of_files = data_manager.read_table_from_file('hr.csv')
    for i in list_of_files:
        birthday_date = i[birthday_index].split('-')
        birthday = date(int(input_date[0]), int(birthday_date[1]), int(birthday_date[2]))
        if birthday in list_of_days:
            employees_names.append(i[name_index])
    return employees_names