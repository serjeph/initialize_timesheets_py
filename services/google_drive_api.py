# google_drive_api.py
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/drive']

TOKEN_PATH = "./google_credential/token.json"

def get_service():
    """
    Authenticates with the Google Drive API and returns a service object.

    This function handles the OAuth2 authentication flow, including:
      - Checking for existing credentials.
      - Refreshing expired credentials.
      - Initiating the authorization flow if no valid credentials are found.

    Returns:
        googleapiclient.discovery.Resource: A service object for interacting with the Google Drive API.
    """    
    creds = None

    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "./google_credential/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    return build("drive", "v3", credentials=creds)


if __name__ == "__main__":
    service = get_service()
    