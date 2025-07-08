#!/usr/bin/python3
import argparse
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload


PATH = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('--op', action="store", dest='op', default="")
parser.add_argument('--fi', action="store", dest='fi', default="")
args = parser.parse_args()

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = PATH + '/serviceAccount.json'
PARENT_FOLDER_ID = "1jt4ZOABV-T5-n30Em3ppCDtPaZbiAqJw"

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds
def getFilesFromFolder():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    results = service.files().list(
    q=f"'{PARENT_FOLDER_ID}' in parents",
    fields="nextPageToken, files(id, name)"
    ).execute()
    return results.get('files', [])

def delete_file(file_id):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    results = service.files().delete(fileId=file_id).execute()
    print(file_id)
    return results

def upload_file(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [PARENT_FOLDER_ID]
    }

    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"File ID: {file.get('id')}")
def findduplicates(file):
    files = getFilesFromFolder()
    for i in files:
        if(i["name"] == os.path.basename(file)):
            delete_file(i["id"])
        else:
            print(os.path.basename(file))
            print(i["name"])

if(args.fi != __file__):
    if(args.op == "I"):
        findduplicates(args.fi)
        upload_file(args.fi)
    elif(args.op == "D"):
        findduplicates(args.fi)
    else:
        print("what the Fuck")


