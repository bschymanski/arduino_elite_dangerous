import json
import time
import serial
from pprint import pprint
import random
import ctypes

# this works only for bytes, so bigger number have to be convertet to individual bytes
# then the bytes can be analysed via theses classes
# https://wiki.python.org/moin/BitManipulation
# "Bit fields, e.g. for communication protocols"
c_uint8 = ctypes.c_uint8
class Flags_bits_0( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("docked",                          c_uint8, 1 ),  # asByte & 1
                ("landed",                          c_uint8, 1 ),  # asByte & 2
                ("Landing_Gear_Down",               c_uint8, 1 ),  # asByte & 4
                ("Shields_Up",                      c_uint8, 1 ),  # asByte & 8
                ("Supercruise",                     c_uint8, 1 ),  # asByte & 16
                ("FlightAssist_Off",                c_uint8, 1 ),  # asByte & 32
                ("Hardpoints_Deployed",             c_uint8, 1 ),  # asByte & 64
                ("In_Wing",                         c_uint8, 1 ),  # asByte & 128
               ]

class Flags_bits_1( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("LightsOn",                        c_uint8, 1 ),  # asByte & 256
                ("Cargo_Scoop_Deployed",            c_uint8, 1 ),  # asByte & 512
                ("Silent_Running",                  c_uint8, 1 ),  # asByte & 1024
                ("Fuel_Scooping",                   c_uint8, 1 ),  # asByte & 2048
                ("Srv_Handbrake",                   c_uint8, 1 ),  # asByte & 4096
                ("Srv_using_Turret_view",           c_uint8, 1 ),  # asByte & 8192
                ("Srv_Turret_retracted",            c_uint8, 1 ),  # asByte & 16384
                ("Srv_DriveAssist",                 c_uint8, 1 ),  # asByte & 32768
               ]

class Flags_bits_2( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("Fsd_MassLocked",                  c_uint8, 1 ),  # asByte & 65536
                ("Fsd_Charging",                    c_uint8, 1 ),  # asByte & 131072
                ("Fsd_Cooldown",                    c_uint8, 1 ),  # asByte & 262144
                ("Low_Fuel",                        c_uint8, 1 ),  # asByte & 524288
                ("Over_Heating",                    c_uint8, 1 ),  # asByte & 1048576
                ("Has_Lat_Long",                    c_uint8, 1 ),  # asByte & 2097152
                ("IsInDanger",                      c_uint8, 1 ),  # asByte & 4194304
                ("Being_Interdicted",               c_uint8, 1 ),  # asByte & 8388608
               ]

class Flags_bits_3( ctypes.LittleEndianStructure ):
    _fields_ = [
                ("In_MainShip",                     c_uint8, 1 ),  # asByte & 16777216
                ("In_Fighter",                      c_uint8, 1 ),  # asByte & 33554432
                ("In_SRV",                          c_uint8, 1 ),  # asByte & 67108864
                ("Hud_in_Analysis_mode",            c_uint8, 1 ),  # asByte & 134217728
                ("Night_Vision",                    c_uint8, 1 ),  # asByte & 268435456
                ("Altitude_from_Average_radius",    c_uint8, 1 ),  # asByte & 536870912
                ("fsdJump",                         c_uint8, 1 ),  # asByte & 1073741824
                ("srvHighBeam",                     c_uint8, 1 ),  # asByte & 2147483648
               ]


class Flags_0( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                  ("bit",    Flags_bits_0 ),
                  ("asByte", c_uint8    )
               ]
flags0 = Flags_0()

class Flags_1( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                  ("bit",    Flags_bits_1 ),
                  ("asByte", c_uint8    )
               ]
flags1 = Flags_1()

class Flags_2( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                  ("bit",    Flags_bits_2 ),
                  ("asByte", c_uint8    )
               ]
flags2 = Flags_2()

class Flags_3( ctypes.Union ):
    _anonymous_ = ("bit",)
    _fields_ = [
                  ("bit",    Flags_bits_3 ),
                  ("asByte", c_uint8    )
               ]
flags3 = Flags_3()

# split big number in individual bytes
#https://www.kite.com/python/answers/how-to-convert-an-int-to-bytes-in-python#:~:text=Use%20int.,the%20beginning%20of%20the%20array.

an_int = 150994952
a_bytes_big = an_int.to_bytes(4, 'little')
print(a_bytes_big)
print(a_bytes_big[0])
print(a_bytes_big[1])
print(a_bytes_big[2])
print(a_bytes_big[3])

flags0.asByte = a_bytes_big[0]
flags1.asByte = a_bytes_big[1]
flags2.asByte = a_bytes_big[2]
flags3.asByte = a_bytes_big[3]

#an_int = 423625720

#print(a_bytes_big[4])
 
#print( "logout: %i"      % flags.bit.logout   )
# `bit` is defined as anonymous field, so its fields can also be accessed directly:
print( "docked                          :  %i" % flags0.docked               )
print( "landed                          :  %i" % flags0.landed               )
print( "Shields_Up                      :  %i" % flags0.Shields_Up    )
print( "Landing_Gear_Down               :  %i" % flags0.Landing_Gear_Down    )
print( "Supercruise                     :  %i" % flags0.Supercruise          )
print( "FlightAssist_Off                :  %i" % flags0.FlightAssist_Off     )
print( "Hardpoints_Deployed             :  %i" % flags0.Hardpoints_Deployed  )
print( "In_Wing                         :  %i" % flags0.In_Wing           )
print( "LightsOn                        :  %i" % flags1.LightsOn           )
print( "Cargo_Scoop_Deployed            :  %i" % flags1.Cargo_Scoop_Deployed           )
print( "Silent_Running                  :  %i" % flags1.Silent_Running           )
print( "Fuel_Scooping                   :  %i" % flags1.Fuel_Scooping           )
print( "Srv_Handbrake                   :  %i" % flags1.Srv_Handbrake           )
print( "Srv_using_Turret_view           :  %i" % flags1.Srv_using_Turret_view           )
print( "Srv_Turret_retracted            :  %i" % flags1.Srv_Turret_retracted           )
print( "Srv_DriveAssist                 :  %i" % flags1.Srv_DriveAssist           )
print( "Fsd_MassLocked                  :  %i" % flags2.Fsd_MassLocked           )
print( "Fsd_Charging                    :  %i" % flags2.Fsd_Charging           )
print( "Fsd_Cooldown                    :  %i" % flags2.Fsd_Cooldown           )
print( "Low_Fuel                        :  %i" % flags2.Low_Fuel           )
print( "Over_Heating                    :  %i" % flags2.Over_Heating           )
print( "Has_Lat_Long                    :  %i" % flags2.Has_Lat_Long           )
print( "IsInDanger                      :  %i" % flags2.IsInDanger           )
print( "Being_Interdicted               :  %i" % flags2.Being_Interdicted           )
print( "In_MainShip                     :  %i" % flags3.In_MainShip           )
print( "In_Fighter                      :  %i" % flags3.In_Fighter           )
print( "In_SRV                          :  %i" % flags3.In_SRV           )
print( "Hud_in_Analysis_mode            :  %i" % flags3.Hud_in_Analysis_mode           )
print( "Night_Vision                    :  %i" % flags3.Night_Vision           )
print( "Altitude_from_Average_radius    :  %i" % flags3.Altitude_from_Average_radius           )
print( "fsdJump                         :  %i" % flags3.fsdJump           )
print( "srvHighBeam                     :  %i" % flags3.srvHighBeam           )

print ("Ready...")
# read file
# please locate the correct Status.json File. This is a testfile -
#with open(r'C:\Users\Anwender\Saved Games\Frontier Developments\Elite Dangerous\Status_test.json', 'r') as myfile:
#    data=myfile.read()

finalstring = "\r"
#ser  = serial.Serial("COM9", baudrate= 9600, 
#        timeout=2.5, 
#        parity=serial.PARITY_NONE, 
#        bytesize=serial.EIGHTBITS, 
#        stopbits=serial.STOPBITS_ONE
#        )

while 1:
    with open(r'C:\Users\Anwender\Saved Games\Frontier Developments\Elite Dangerous\Status_test.json', 'r') as myfile:
        data=myfile.read()
    
    obj = json.loads(data)
    an_int = obj['Flags']
    a_bytes_big = an_int.to_bytes(4, 'little')
    print(a_bytes_big)
    print(a_bytes_big[0])
    print(a_bytes_big[1])
    print(a_bytes_big[2])
    print(a_bytes_big[3])

    flags0.asByte = a_bytes_big[0]
    flags1.asByte = a_bytes_big[1]
    flags2.asByte = a_bytes_big[2]
    flags3.asByte = a_bytes_big[3]
    
    Pips_obj = obj['Pips']

    print( "docked                          :  %i" % flags0.docked               )
    print( "landed                          :  %i" % flags0.landed               )
    print( "Shields_Up                      :  %i" % flags0.Shields_Up    )
    print( "Landing_Gear_Down               :  %i" % flags0.Landing_Gear_Down    )
    print( "Supercruise                     :  %i" % flags0.Supercruise          )
    print( "fuelMain                        :  %i" % int(obj['Fuel']['FuelMain']))
    print( "fuelReserve                     :  %i" % int(obj['Fuel']['FuelReservoir']*1000))
    print( "Cargo                           :  %i" % int(obj['Cargo']))
    print( "LegalState                      :  " + obj['LegalState'])
    print( "Pips System                     :  %i" %int(Pips_obj[0]))
    print( "Pips Engine                     :  %i" %int(Pips_obj[1]))
    print( "Pips Weapons                    :  %i" %int(Pips_obj[2]))
    #print( "FlightAssist_Off                :  %i" % flags0.FlightAssist_Off     )
    #print( "Hardpoints_Deployed             :  %i" % flags0.Hardpoints_Deployed  )
    #print( "In_Wing                         :  %i" % flags0.In_Wing           )
    print( "LightsOn                        :  %i" % flags1.LightsOn           )
    #print( "Cargo_Scoop_Deployed            :  %i" % flags1.Cargo_Scoop_Deployed           )
    #print( "Silent_Running                  :  %i" % flags1.Silent_Running           )
    #print( "Fuel_Scooping                   :  %i" % flags1.Fuel_Scooping           )
    #print( "Srv_Handbrake                   :  %i" % flags1.Srv_Handbrake           )
    #print( "Srv_using_Turret_view           :  %i" % flags1.Srv_using_Turret_view           )
    #print( "Srv_Turret_retracted            :  %i" % flags1.Srv_Turret_retracted           )
    #print( "Srv_DriveAssist                 :  %i" % flags1.Srv_DriveAssist           )
    #print( "Fsd_MassLocked                  :  %i" % flags2.Fsd_MassLocked           )
    #print( "Fsd_Charging                    :  %i" % flags2.Fsd_Charging           )
    #print( "Fsd_Cooldown                    :  %i" % flags2.Fsd_Cooldown           )
    #print( "Low_Fuel                        :  %i" % flags2.Low_Fuel           )
    #print( "Over_Heating                    :  %i" % flags2.Over_Heating           )
    #print( "Has_Lat_Long                    :  %i" % flags2.Has_Lat_Long           )
    #print( "IsInDanger                      :  %i" % flags2.IsInDanger           )
    #print( "Being_Interdicted               :  %i" % flags2.Being_Interdicted           )
    #print( "In_MainShip                     :  %i" % flags3.In_MainShip           )
    #print( "In_Fighter                      :  %i" % flags3.In_Fighter           )
    #print( "In_SRV                          :  %i" % flags3.In_SRV           )
    #print( "Hud_in_Analysis_mode            :  %i" % flags3.Hud_in_Analysis_mode           )
    #print( "Night_Vision                    :  %i" % flags3.Night_Vision           )
    #print( "Altitude_from_Average_radius    :  %i" % flags3.Altitude_from_Average_radius           )
    #print( "fsdJump                         :  %i" % flags3.fsdJump           )
    #print( "srvHighBeam                     :  %i" % flags3.srvHighBeam           )
    serial_string = str(flags0.docked)+str(flags0.landed)+str(flags0.Shields_Up)+str(flags0.Landing_Gear_Down)+str(flags0.Supercruise)+"ps"+str(obj['Pips'][0])+"pe"+str(obj['Pips'][1])+"pw"+str(obj['Pips'][2])
    
    #ser.write(serial_string.encode("utf-8"))
    #ser.write(finalstring.encode("utf-8"))
    print ("Ready...")

    time.sleep(1)

    

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
