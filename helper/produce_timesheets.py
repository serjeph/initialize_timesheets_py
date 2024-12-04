# produce_timesheets.py

from services.google_drive_api import get_service

service = get_service()

def copy_gsheets(file_id, folder_id, new_title):
    """
    Copies a Google Sheet to a specified folder with a new title.

    Args:
        file_id (str): The ID of the Google Sheet to copy.
        folder_id (str): The ID of the folder to copy the sheet to.
        new_title (str): The new title for the copied sheet.

    Returns:
        str: The ID of the newly copied sheet, or None if an error occurred.
    """
    try:
        copied_file = service.files().copy(
            fileId = file_id,
            body = {
                'parents': [folder_id],
                'name' : new_title,
            },
            supportsAllDrives = True
        ).execute()

        print(f"Timesheet created successfully! New file ID: [{copied_file['id']}] New file name: [{new_title}]")
        return copied_file['id']
    
    except Exception as ex:
        print(f'An error occurred: {ex}')
        return None
    