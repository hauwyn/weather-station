import shutil
import datetime
import os
import time

file = "/media/pi/USB"
while True:
    if os.path.ismount(file):
        file = "/home/pi/weather.db"
        destination = "/media/pi/USB/backup_%s.db" % datetime.datetime.now().date()
    
        try:
           shutil.copy2(file, destination)
        except shutil.Error as e:
           print("Error: %s" % e)
        except IOError as e:
           print("Error: %s" % e.strerror)
    if not os.path.ismount(file):
        final = "/media/pi/USB/backup_%s.db" % datetime.datetime.now().date()
        if os.path.isfile(final):
            print ("Successful!")
            break
        else:
            print("Error!")
    time.sleep(5)        
