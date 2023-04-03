
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


sheet = service.spreadsheets()
range = 'users!B2:E1000'


rows = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range).execute().get('values', [])
 
 #reading rows one by one
complete_emails = []
email_data = {}
for i,row in enumerate(rows):
    for key,values in enumerate(row):
         #print(f"Cell {chr(key + 65)}{i+1} contains {values}")  #i+1 we are ignoring the header row so adding 1 to set exact value
          
         if (key)==2:   
          email = row[key]   
         # complete_emails.append(email)
          email_data[email]= row
#-------------------------------- 
#/home/runner/work/onboarding-infomagnus/onboarding-infomagnus/
file=open("completed.txt", "r")  
fileRead = open("completed.txt","a")  
content = file.read()    
for emailkey,emailvalue in enumerate(email_data):
   #print(emailvalue)
   #print(email_data[emailvalue])
  # Open the file for reading
 
    # Read each line of the file
  if emailvalue not in content:
    
   # print("The string does not exist in the file."+emailvalue)
    fileRead.write(emailvalue+"\n") 
   # print(email_data[emailvalue])
    outputdata = (email_data[emailvalue])
    outputdata = ', '.join(outputdata)
  #  outputdata = '"'+outputdata+'"'
    print(outputdata)
    break

file.close()  
fileRead.close()             
              


          
