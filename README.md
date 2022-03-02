# arduino_elite_dangerous
Button and Status Box for Elite Dangerous

# Windows Side
install python
install pyserial (https://stackoverflow.com/questions/41199876/attributeerror-module-serial-has-no-attribute-serial)

locate and read the Elite Dangerous Status File (https://elite-journal.readthedocs.io/en/latest/Status%20File/)

Example: 
{ "timestamp":"2022-02-27T10:49:26Z", "event":"Status", "Flags":150994952, "Flags2":0, "Pips":[8,4,0], "FireGroup":0, "GuiFocus":0, "Fuel":{ "FuelMain":32.000000, "FuelReservoir":0.254654 }, "Cargo":0.000000, "LegalState":"Clean", "Balance":1110431641 }

Read Json File (https://pythonbasics.org/read-json-file/)
If Syntax Error: https://exerror.com/syntaxerror-unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-truncated-uxxxxxxxx-escape/#:~:text=UXXXXXXXX%20escape%20Error%20%3F-,To%20Solve%20SyntaxError%3A%20(unicode%20error)%20'unicodeescape'%20codec,double%20quotes%20and%20forwardslash%20character.

Sending Json to serial and receive on arduino
(https://stackoverflow.com/questions/55698070/sending-json-over-serial-in-python-to-arduino)

Bit manipulation
https://wiki.python.org/moin/BitManipulation

int to multiple bytes
https://www.geeksforgeeks.org/how-to-convert-int-to-bytes-in-python/

print individual bits from a number
https://www.tutorialspoint.com/read-a-specific-bit-of-a-number-with-arduino