import mysql.connector #importerer de nødvendige libraries'ene
import datetime
import pyfirmata
import time

board = pyfirmata.Arduino('COM6') 

it = pyfirmata.util.Iterator(board) 

it.start() 

board.analog[1].enable_reporting()

analog_read = board.get_pin('a:1:i')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elev",
    database="3elda",
) #her kobler koden seg på SQL serveren

mycursor = mydb.cursor()

print("Connected...")

sql = "INSERT INTO sensor(verdi, tid) VALUES (%s,%s)" #setter in verdi 1 og tidspunkt inni table'en med navnet "sensor"


print("Done")

while True:
    print(analog_read.read())
    time.sleep(2)

    verdi = 1.0

    tid = datetime.datetime.now()

    val = (analog_read.read(), tid)

    mycursor.execute(sql, val)
    mydb.commit()   
