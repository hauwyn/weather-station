import os,sys
from datetime import datetime
from sense_hat import SenseHat
import glob

sense = SenseHat()
collect_date = datetime.today()
collect_date = collect_date.strftime("%Y-%m-%d")
list_of_files = glob.glob('/media/pi/USB/*.csv')  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
for file in os.listdir("/media/pi/USB/"):
    if collect_date in file:
        print (latest_file)
        print("copy done!")
        sense.show_message("Copy Done!")
        sense.show_message(latest_file)
        break
if not collect_date in file:
    print ("Try again!")
    sense.show_message("Try again!")
        

