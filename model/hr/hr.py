""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util
# import csv


DATAFILE = "model/hr/hr.csv"
# DATAFILE = 'C:/1Code/Projects/secure-erp-python-mateuszski/model/hr/hr.csv'
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def list_employees():
    # with open(DATAFILE, newline='') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=';')
    #     for row in reader:
    #         # print(row)
    #         return row
    table = data_manager.read_table_from_file(DATAFILE)
    return table, HEADERS


def add_employee():
    added = data_manager.write_table_to_file(DATAFILE)
    return added, HEADERS


def update_employee():
    pass

def delete_employee():
    pass

def