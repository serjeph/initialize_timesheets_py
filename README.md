# Annual Timesheet Generator

This Python script automates the process of creating timesheets for employees by copying a Google Sheet template.

## How it Works

The script reads a list of employee names from a text file (`employee_list.txt`) and uses the Google Drive API to create a copy of a template Google Sheet for each employee. The new timesheets are named "{year}作業日報_{employee_name}" and placed in a specified Google Drive folder.

## Prerequisites

- **Python 3.6 or higher**
- **Google Cloud Project:** With the Drive API enabled.
- **Credentials:** Obtain OAuth2 credentials for your Google Cloud project and save them as `credentials.json` in the `google_credential` directory.
- **Template Sheet:** A Google Sheet to use as a template for the timesheets.
- **Employee List:** A text file named `employee_list.txt` containing a list of employee names, one per line.

## Setup

1. **Install Dependencies:**
    ```
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib python-dotenv
    ```
2. **Set Environment Variables:**
   - Create a `.env` file in the project root directory.
   - Add the following environment variables:

        ```
        FOLDER_ID=google_drive_folder_id
        FILE_ID=template spreadsheet id
        ```
        - Replace `google_drive_id` with the ID of the Google Drive folder where you want to store the timesheets.
        - Replace `template spreadsheet id` with the ID of your Google Sheet timesheet template.

3. **Authenticate with the Google Drive:**
   - Run the script (`python main.py`).
   - The script will guide you through the OAuth2 authentication flow if you haven't already authorized the application.
   - A `token.json` file will be created in the `google_credential` directory to store your credentials.

## Usage

1. Update `employee_list.txt`: Make sure the file contains the names of all employees who need timesheets.

2. Run the script:
    ```
    python main.py
    ```

## Notes
- The script assumens that the template sheet and the `employee_list.txt` file are in the same directory as the script.
- You can modify the script to customize the naming convention for the timesheet or to add additional functionality.
- Make sure the Google Drive API is enabled in your Google Cloud project.
- If you encounter any issues, refer to the  [Google Drive API Documentation](https://developers.google.com/drive/api/v3/about) for troubleshooting.   
