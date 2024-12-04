# main.py
import os
from dotenv import load_dotenv

from helper.produce_timesheets import copy_gsheets

load_dotenv()

def main():
    """
    Copies a Google Sheet template for each employee listed in a text file.

    This script reads employee names from 'employee_list.txt' and uses the 
    `copy_gsheets` function to create a copy of a template Google Sheet 
    for each employee. The new sheets are named "2025作業日報_{employee_name}" 
    and placed in the Google Drive folder specified by the `FOLDER_ID` environment variable.

    Environment Variables:
        FOLDER_ID: The ID of the Google Drive folder where the copied sheets will be stored.
        FILE_ID: The ID of the template Google Sheet to be copied.
    """
    try:
        with open('employee_list.txt', 'r', encoding='utf-8') as employees:
            for employee in employees:
                # Remove potential newline characters from employee name
                employee_name = employee.strip()
                copy_gsheets(os.getenv('FILE_ID'), os.getenv('FOLDER_ID'), f"2025作業日報_{employee_name}")

    except Exception as ex:
        print(f"Error occurred: {ex}")

if __name__ == "__main__":
    main()