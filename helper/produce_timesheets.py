# produce_timesheets.py

def copy_gsheets(service, file_id, folder_id, new_title):
    

    try:
        copied_file = service.files().copy(
            fileId = file_id,
            body = {
                'parents': [folder_id],
                'name' : new_title
            }
        ).execute()

        print(f'File copied successfully! New file ID: {copied_file["id"]}')
        return copied_file["id"]
    
    except Exception as e:
        print(f'An error occurred: {e}')
        return None
    