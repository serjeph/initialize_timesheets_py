# export.py
import os
from dotenv import load_dotenv
load_dotenv()

def output_ids(directory, employee_name,  spreadsheet_id, filename='employees.txt'):

    try:
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # Construct the full output file path
        output_path = os.path.join(directory, filename)

        # Open the text file in append mode ('a')
        with open(output_path, 'a', encoding='utf-8') as output:
            output.write(f"{employee_name} $ {spreadsheet_id}\n")

    except Exception as ex:
        print(f"Error occurred: {ex}")
