from time import sleep
import mysql.connector
from datetime import datetime

dbConnection = mysql.connector.connect(
	host="54.254.127.82",
	user="gps2020",
	password="gps#2020#123",
	database="pelacakan"
)




while True : 
	try:
		file = open("/home/pi/data.txt","r").read()
		print(file)
		split = file.split(" | ")
		time = datetime.now()
		lat = split[2].replace(" Lat: " ,"")
		long = split[3].replace(" Lon: ","")
		altitude = split[4].replace(" Alt: " ,"")
	
		sql 	= "INSERT INTO gps_log (latitude,longitude,timestamp,altitude) values(%s,%s,%s,%s)"
		values 	= (lat,long,time,altitude)
		cursor 	= dbConnection.cursor()
		cursor.execute(sql,values)
		dbConnection.commit()
		cursor.close() 

		sleep(1)
	except Exception as e :
		continue
