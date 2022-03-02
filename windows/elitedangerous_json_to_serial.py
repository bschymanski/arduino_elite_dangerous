import json
import time
import serial
from pprint import pprint
import random
import ctypes

c_uint8 = ctypes.c_uint8

class Flags_bits( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("docked",                          c_uint8, 1 ),  # asByte & 1
                ("landed",                          c_uint8, 1 ),  # asByte & 2
                ("Landing_Gear_Down",               c_uint8, 1 ),  # asByte & 4
                ("Shields_Up",                      c_uint8, 1 ),  # asByte & 8
                ("Supercruise",                     c_uint8, 1 ),  # asByte & 16
                ("FlightAssist_Off",                c_uint8, 1 ),  # asByte & 32
                ("Hardpoints_Deployed",             c_uint8, 1 ),  # asByte & 64
                ("In_Wing",                         c_uint8, 1 ),  # asByte & 128
                ("LightsOn",                        c_uint8, 1 ),  # asByte & 256
                ("Cargo_Scoop_Deployed",            c_uint8, 1 ),  # asByte & 512
                ("Silent_Running",                  c_uint8, 1 ),  # asByte & 1024
                ("Fuel_Scooping",                   c_uint8, 1 ),  # asByte & 2048
                ("Srv_Handbrake",                   c_uint8, 1 ),  # asByte & 4096
                ("Srv_using_Turret_view",           c_uint8, 1 ),  # asByte & 8192
                ("Srv_Turret_retracted",            c_uint8, 1 ),  # asByte & 16384
                ("Srv_DriveAssist",                 c_uint8, 1 ),  # asByte & 32768
                ("Fsd_MassLocked",                  c_uint8, 1 ),  # asByte & 65536
                ("Fsd_Charging",                    c_uint8, 1 ),  # asByte & 131072
                ("Fsd_Cooldown",                    c_uint8, 1 ),  # asByte & 262144
                ("Low_Fuel",                        c_uint8, 1 ),  # asByte & 524288
                ("Over_Heating",                    c_uint8, 1 ),  # asByte & 1048576
                ("Has_Lat_Long",                    c_uint8, 1 ),  # asByte & 2097152
                ("IsInDanger",                      c_uint8, 1 ),  # asByte & 4194304
                ("Being_Interdicted",               c_uint8, 1 ),  # asByte & 8388608
                ("In_MainShip",                     c_uint8, 1 ),  # asByte & 16777216
                ("In_Fighter",                      c_uint8, 1 ),  # asByte & 33554432
                ("In_SRV",                          c_uint8, 1 ),  # asByte & 67108864
                ("Hud_in_Analysis_mode",            c_uint8, 1 ),  # asByte & 134217728
                ("Night_Vision",                    c_uint8, 1 ),  # asByte & 268435456
                ("Altitude_from_Average_radius",    c_uint8, 1 ),  # asByte & 536870912
                ("fsdJump",                         c_uint8, 1 ),  # asByte & 1073741824
                ("srvHighBeam",                     c_uint8, 1 ),  # asByte & 2147483648
               ]


class Flags( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                  ("bit",    Flags_bits ),
                  ("asByte", c_uint8    )
               ]
flags = Flags()

flags.asByte = 423625720  # ->0010

#an_int = 423625720
an_int = 514
a_bytes_big = an_int.to_bytes(5, 'big')
print(a_bytes_big)
print(a_bytes_big[0])
print(a_bytes_big[1])
print(a_bytes_big[2])
print(a_bytes_big[3])
print(a_bytes_big[4])
 
#print( "logout: %i"      % flags.bit.logout   )
# `bit` is defined as anonymous field, so its fields can also be accessed directly:
print( "docked                          :  %i" % flags.docked               )
print( "landed                          :  %i" % flags.landed               )
print( "Shields_Up                      :  %i" % flags.Shields_Up    )
print( "Landing_Gear_Down               :  %i" % flags.Landing_Gear_Down    )
print( "Supercruise                     :  %i" % flags.Supercruise          )
print( "FlightAssist_Off                :  %i" % flags.FlightAssist_Off     )
print( "Hardpoints_Deployed             :  %i" % flags.Hardpoints_Deployed  )
print( "In_Wing                         :  %i" % flags.In_Wing           )
print( "LightsOn                        :  %i" % flags.LightsOn           )
print( "Cargo_Scoop_Deployed            :  %i" % flags.Cargo_Scoop_Deployed           )
print( "Silent_Running                  :  %i" % flags.Silent_Running           )
print( "Fuel_Scooping                   :  %i" % flags.Fuel_Scooping           )
print( "Srv_Handbrake                   :  %i" % flags.Srv_Handbrake           )
print( "Srv_using_Turret_view           :  %i" % flags.Srv_using_Turret_view           )
print( "Srv_Turret_retracted            :  %i" % flags.Srv_Turret_retracted           )
print( "Srv_DriveAssist                 :  %i" % flags.Srv_DriveAssist           )
print( "Fsd_MassLocked                  :  %i" % flags.Fsd_MassLocked           )
print( "Fsd_Charging                    :  %i" % flags.Fsd_Charging           )
print( "Fsd_Cooldown                    :  %i" % flags.Fsd_Cooldown           )
print( "Low_Fuel                        :  %i" % flags.Low_Fuel           )
print( "Over_Heating                    :  %i" % flags.Over_Heating           )
print( "Has_Lat_Long                    :  %i" % flags.Has_Lat_Long           )
print( "IsInDanger                      :  %i" % flags.IsInDanger           )
print( "Being_Interdicted               :  %i" % flags.Being_Interdicted           )
print( "In_MainShip                     :  %i" % flags.In_MainShip           )
print( "In_Fighter                      :  %i" % flags.In_Fighter           )
print( "In_SRV                          :  %i" % flags.In_SRV           )
print( "Hud_in_Analysis_mode            :  %i" % flags.Hud_in_Analysis_mode           )
print( "Night_Vision                    :  %i" % flags.Night_Vision           )
print( "Altitude_from_Average_radius    :  %i" % flags.Altitude_from_Average_radius           )
print( "fsdJump                         :  %i" % flags.fsdJump           )
print( "srvHighBeam                     :  %i" % flags.srvHighBeam           )

print ("Ready...")
# read file
# please locate the correct Status.json File. This is a testfile -
with open(r'C:\Users\Anwender\Saved Games\Frontier Developments\Elite Dangerous\Status_test.json', 'r') as myfile:
    data=myfile.read()

ser  = serial.Serial("COM9", baudrate= 9600, 
           timeout=2.5, 
           parity=serial.PARITY_NONE, 
           bytesize=serial.EIGHTBITS, 
           stopbits=serial.STOPBITS_ONE
        )

#while 1:
#    # parse file
#    data_dump = json.dumps(data)
#    print(data_dump)
#    obj = json.loads(data)
#    Fuel_obj = obj['Fuel']
#    Pips_obj = obj['Pips']
#    # show values
#    doc = "0010100010001110001"
#    print("Flags: " + str(obj['Flags']))
#    print("Pips: " + str(obj['Pips']))
#    print("Pips System: " + str(Pips_obj[0]))
#    print("Fuel: " + str(obj['Fuel']))
#    print("FuelMain: " + str(Fuel_obj['FuelMain']))
#    str_flags = str(obj['Flags'])
#    print("str_flags : " + str_flags)
#    finalstring = "\r"
#    ser.write(doc.encode("utf-8"))
#    ser.write(finalstring.encode("utf-8"))
#
#    time.sleep(1)
