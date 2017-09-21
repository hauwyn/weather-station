#!/usr/bin/python
import os
from sense_hat import SenseHat
import time
import sys
import sqlite3
from datetime import datetime
import csv

db = "/home/pi/Desktop/weather.db"
#db = "weather.db"

connection = sqlite3.connect(db)
#with sqlite3.connect(db) as connection:
c = connection.cursor()
c.execute( """ CREATE TABLE IF NOT EXISTS weather_table(
                                        Date text,
                                        Temp float,
                                        Humidity float,
                                        Pressure float
                                    )""")
'''# detect the CPU temperature
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return(t)
'''
'''#create the file with header (however it need to be included in the loop, or it may cannot create the file at 0 o'clock! ) 
collect_date = datetime.today()
collect_date = collect_date.strftime("%Y-%m-%d")

file = '/home/pi/weather_data/'+collect_date +'.csv' #create file named weather_data in /home/pi/
file_exists = os.path.isfile(file)

with open (file, 'a') as csvfile:
    headers = ['Date', 'Temperature', 'Humidity','Pressure']
    writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)

    if not file_exists:
        writer.writeheader()
'''
try:
    while True:
        collect_date = datetime.today()
        collect_date = collect_date.strftime("%Y-%m-%d")

        file = '/home/pi/weather_data/' + collect_date + '.csv'  # create file named weather_data in /home/pi/
        file_exists = os.path.isfile(file)

        with open(file, 'a') as csvfile:
            headers = ['Date', 'Temperature', 'Humidity', 'Pressure']
            writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)

            if not file_exists:
                writer.writeheader()

        sense = SenseHat()
        sense.clear()
        t1 = sense.get_temperature_from_humidity()
        t2 = sense.get_temperature_from_pressure()
        #t_cpu = get_cpu_temp()
        calibrated_temp = 14
        temp = (t1 + t2 - calibrated_temp) / 2
       # temp = temp-((t_cpu-temp) / 0.8)
        temp = round(temp, 1)
        print("Temperature:", temp)

        calibrated_humidity = 15
        humidity = sense.get_humidity() + calibrated_humidity
        humidity = round(humidity, 1)
        print("Humidity:", humidity)

        pressure = sense.get_pressure()
        pressure = round(pressure, 1)
        print("Pressure:", pressure)
        
        date = datetime.now()
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        print ("date:", date)
    
        with sqlite3.connect(db) as connection:
            c = connection.cursor()
            c.execute("INSERT INTO weather_table VALUES(?,?,?,?);", (date,temp,humidity,pressure))
        
        with open (file, 'a') as csvfile:
            csvfile.write("{}, {},{},{}\n".format(date,temp,humidity,pressure))
        
        time.sleep(600)         
            
except KeyboardInterrupt:
    pass 
               

