import dropbox
import requests
import time
from datetime import datetime,timedelta
"""upload a file to Dropbox using API v2
        """
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "lspdxnfLqdAAAAAAAAAAC3ZGTCjWXnHJgeydKRK8inim4T3N_MWUFwzz0vO4En1v" # API v2
    transferData = TransferData(access_token)

    collect_date = datetime.today()
    collect_date = collect_date.strftime("%Y-%m-%d")
    file_from = "/home/pi/Desktop/weather1.db"
    date= datetime.now()
    date = date.strftime("%Y-%m-%d %H:%M:%S")
    file_to = '/weather/'+date+'.db'  # The full path to upload the file to, including the file name
    
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
