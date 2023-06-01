# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: A script to demostrate pickling and error exception handling
# ChangeLog (Who,When,What):
# Wparks,30May2023,Created script
# ---------------------------------------------------------------------------- #

import pickle

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    with open('file_name','wb') as f:
        pickle.dump(list_of_data,f)


def read_data_from_file(file_name):
    with open('file_name', 'rb') as f:
        list_of_data = pickle.load(f)
        return list_of_data

# Presentation ------------------------------------ #

customer_name = input('Please enter the name of the customer:')
customer_ID = input('Please enter the ID of the customer:')
name_ID = customer_name + ' ' + customer_ID
lstCustomer.append(name_ID)
save_data_to_file(file_name=strFileName, list_of_data=lstCustomer)
print(f'{read_data_from_file(file_name=strFileName)} was saved and read to and from a binary file')

