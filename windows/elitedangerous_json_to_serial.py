import json
import time


# read file
# please locate the correct Status.json File. This is a testfile
with open(r'C:\Users\Anwender\Saved Games\Frontier Developments\Elite Dangerous\Status_test.json', 'r') as myfile:
    data=myfile.read()

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
    time.sleep(1)
