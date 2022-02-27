import json
import time
import serial
from pprint import pprint
import random

print ("Ready...")
# read file
# please locate the correct Status.json File. This is a testfile -
with open(r'C:\Users\Anwender\Saved Games\Frontier Developments\Elite Dangerous\Status_test.json', 'r') as myfile:
    data=myfile.read()

ser  = serial.Serial("COM8", baudrate= 9600, 
           timeout=2.5, 
           parity=serial.PARITY_NONE, 
           bytesize=serial.EIGHTBITS, 
           stopbits=serial.STOPBITS_ONE
        )

while 1:
    # parse file
    data_dump = json.dumps(data)
    print(data_dump)
    obj = json.loads(data)
    Fuel_obj = obj['Fuel']
    Pips_obj = obj['Pips']
    # show values
    print("Flags: " + str(obj['Flags']))
    print("Pips: " + str(obj['Pips']))
    print("Pips System: " + str(Pips_obj[0]))
    print("Fuel: " + str(obj['Fuel']))
    print("FuelMain: " + str(Fuel_obj['FuelMain']))
    if ser.isOpen():
        ser.write(data_dump.encode('ascii'))
        ser.flush()
        try:
            incoming = ser.readline().decode("utf-8")
            print (incoming)
        except Exception as e:
            print (e)
            pass
        ser.close()
    else:
        print ("opening error")
    time.sleep(1)
