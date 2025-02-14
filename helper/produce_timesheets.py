# produce_timesheets.py

from services.google_drive_api import get_service

def copy_gsheets(file_id, folder_id, new_title, service = get_service()):
    
    try:
        copied_file = service.files().copy(
            fileId = file_id,
            body = {
                'parent': [folder_id],
                'name' : new_title,
                'supportsAllDrives': True
            }
        ).execute()

        print(f'File copied successfully! New file ID: {copied_file["id"]}')
        return copied_file["id"]
    
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
    

if __name__ == "__main__":
    service = get_service()
    copy_gsheets()