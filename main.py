# main.py
import os

from dotenv import load_dotenv
from helper.produce_timesheets import copy_gsheets
load_dotenv()
FILE_ID = os.getenv('FILE_ID')
FOLDER_ID = os.getenv('FOLDER_ID')

def main():

    employee_list_path = "employee_list.txt"
    try:
        with open(employee_list_path, "r") as employees:
            for employee in employees:
                copy_gsheets(FILE_ID, 
                             FOLDER_ID,
                             f"2025作業日報_{employee}")

    except Exception as e:
        print(f'An error occurred: {e}')  
                
if __name__ == "__main__":
    main()