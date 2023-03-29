
from googleapiclient.discovery import build

from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'infomagnus-onboarding.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1q6rW7kFGXxivDI2YCO39g308cMfykNOiqOqhx7r4q48'
 


service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
sheet = service.spreadsheets()
#result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Sales!A1:G2").execute()
#rowcount = sheet.values().get(SAMPLE_SPREADSHEET_ID, range="Sales!A1:G2").execute().getValues().size()
#values = result.get('values', [])
range = 'users!B:D'


rows = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range).execute().get('values', [])
last_row = rows[-1] if rows else None
last_row_id = len(rows)
#print(last_row_id, last_row)
print(last_row)
 
 
