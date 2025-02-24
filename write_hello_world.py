from google.oauth2 import service_account
from googleapiclient.discovery import build

# Google Sheets ID and range you want to write to
SPREADSHEET_ID = '1GCrE2YiAWnB0pQk43i5_rawGpqrkgGj5yBanfg74gT8'
RANGE_NAME = 'Sheet1!A1'  # Adjust to the specific cell or range as needed

# Load the service account credentials
credentials = service_account.Credentials.from_service_account_file(
    'november-440715-2fddde9bed92.json',
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)

# Build the Sheets API service
service = build('sheets', 'v4', credentials=credentials)

# The data to be added
values = [["Hello World"]]
body = {
    'values': values
}

# Call the Sheets API to update the spreadsheet
result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE_NAME,
    valueInputOption="RAW",
    body=body).execute()

print(f"{result.get('updatedCells')} cells updated.")
