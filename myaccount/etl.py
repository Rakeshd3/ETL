import gspread
from google.auth.exceptions import RefreshError
from google.oauth2.service_account import Credentials
import pandas as pd

# Define the correct scope for Google Drive API
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file']

# Load the service account credentials from a JSON key file
credentials = Credentials.from_service_account_file('gs_credentials.json',
                                                    scopes=scope)

url = 'https://docs.google.com/spreadsheets/d/1F3ZFadJXIn6rTRzPKIFm3poAk67-0dlk/edit?usp=drive_link&ouid=106187126285213171434&rtpof=true&sd=true'

try:
    client = gspread.authorize(credentials)
    # client = gspread.service_account(filename='gs_credentials.json')
    worksheet = client.open('RawData.xlsx').worksheet('raw data')

    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    df.to_csv('raw_data.csv', index=False)
    # Print the data (as a list of lists)
    # sheet.share('rakeshdash6180@gmail.com', perm_type="user", role='writer')
except RefreshError as e:
    print(e.__str__())
except Exception as e:
    print(e.__str__())
else:
    print("Success: Google opened")
    # sheet.column_count()
