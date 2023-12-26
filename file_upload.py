from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
from fastapi.responses import JSONResponse
import os
import io
from googleapiclient.errors import HttpError

scope = ['https://www.googleapis.com/auth/drive']
service_account_json_key = 'credentials.json'
credentials = service_account.Credentials.from_service_account_file(
                              filename=service_account_json_key,
                              scopes=scope)
service = build('drive', 'v3', credentials=credentials)

def is_valid_format(file_name: str,VALID_FORMATS:list) -> bool:
    _, file_extension = os.path.splitext(file_name)
    return file_extension.lower()[1:] in VALID_FORMATS
def upload_file_to_drive(file_path, folder_name,VALID_FORMATS:list):
    if not is_valid_format(os.path.basename(file_path),VALID_FORMATS):
        return None  # Invalid format
    # Get the ID of the target folder
    folder_query = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'"
    results = service.files().list(q=folder_query).execute()
    folder_id = results.get('files', [])[0]['id'] if results.get('files', []) else None

    # If the folder doesn't exist, create it
    if not folder_id:
        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        folder_id = folder.get('id')

    # Create a media file upload instance with the file path and MIME type
    media = MediaFileUpload(file_path, mimetype='application/octet-stream')

    # Define the file metadata, including the file name and parent folder ID
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }

    try:
        # Upload the file to Google Drive
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        # Get the file ID
        file_id = file.get('id')

        # Define the permission for the file (make it publicly accessible)
        permission_metadata = {
            'role': 'reader',
            'type': 'anyone'
        }

        # Create the permission for the file
        permission = service.permissions().create(fileId=file_id, body=permission_metadata).execute()

        # Get the URL of the file
        file_url = f"https://drive.google.com/uc?id={file_id}"

        print(f'File ID: {file_id}')
        print(f'File URL: {file_url}')

        return file_url
    except HttpError as error:
        print('An error occurred: %s' % error)
        return None


def upload_file_to_drive_url(file_path:str, folder_name:str,VALID_FORMATS:list):
    # Call the function to upload the file to Google Drive
    file_url = upload_file_to_drive(file_path, folder_name,VALID_FORMATS)
    if file_url:
        return JSONResponse(content={"file_url": file_url}, status_code=200)
    else:
        return JSONResponse(content={"error": "Failed to upload file"}, status_code=500)