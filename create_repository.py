import gspread
from google.oauth2.service_account import Credentials
from github import Github

# Authenticate with Google Sheets API
creds = Credentials.from_service_account_file('google-creds.json')
client = gspread.authorize(creds)
sheet = client.open('responses').sheet1

# Authenticate with GitHub API
g = Github('access_token')

# Get the last row of the sheet
row = len(sheet.get_all_values())

# Get the role from the form
role = sheet.cell(row, 2).value

# Get the template repository based on the role
if role == 'developer':
    template_repo = g.get_repo('docs')
elif role == 'designer':
    template_repo = g.get_repo('owner/designer-template')
# add more conditionals for each role

# Create the new repository
new_repo = g.get_user().create_repo('new-repo', private=True)

# Clone the template repository
template_contents = template_repo.get_contents('')
for content_file in template_contents:
    content = template_repo.get_contents(content_file.path).decoded_content
    new_repo.create_file(content_file.path, 'initial commit', content)

# Assign issues based on the role
if role == 'developer':
    issue = new_repo.create_issue(title='Developer issue', body='Assign to a developer')
    issue.add_to_labels('developer')
elif role == 'designer':
    issue = new_repo.create_issue(title='Designer issue', body='Assign to a designer')
    issue.add_to_labels('designer')
# add more conditionals for each role
