import board
from digitalio import DigitalInOut, Pull
from adafruit_debouncer import Debouncer
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

#button_in = DigitalInOut(board.GP10) # defaults to input
#button_in.pull = Pull.UP # turn on internal pull-up resistor
#button = Debouncer(button_in)
pins = (board.GP6, board.GP7, board.GP8, board.GP9,board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21)
buttons = []   # will hold list of Debouncer objects
for pin in pins:   # set up each pin
    tmp_pin = DigitalInOut(pin) # defaults to input
    tmp_pin.pull = Pull.UP      # turn on internal pull-up resistor
    buttons.append( Debouncer(tmp_pin) )

while True:
    for i in range(len(buttons)):
        buttons[i].update()
        if buttons[i].fell:
            print("button",i,"pressed!")
            if i == 0:
                print("Landing Gear")
                kbd.send(Keycode.L)
            if i == 6:
                print("Cargo Scoop")
                kbd.send(Keycode.NINE)
            if i == 9:
                print("Light ON")
                kbd.send(Keycode.SEVEN)
            if i == 12:
                print("Night Vision")
                kbd.send(Keycode.COMMA)
            if i == 1:
                print("Galaxy Map")
                kbd.send(Keycode.PERIOD)
            if i == 4:
                print("FSD Junp")
                kbd.send(Keycode.J)
            if i == 10:
                print("Supercruise")
                kbd.send(Keycode.EIGHT)
            if i == 13:
                print("HUD Analysis")
                kbd.send(Keycode.M)
            if i == 3:
                print("System Map")
                kbd.send(Keycode.KEYPAD_MINUS)
            if i == 5:
                print("Heat Sink")
                kbd.send(Keycode.V)
            if i == 8:
                print("Shield Cell")
                kbd.send(Keycode.SIX)
            if i == 14:
                print("Hard Points")
                kbd.send(Keycode.U)
            if i == 2:
                print("System")
                kbd.send(Keycode.LEFT_ARROW)
            if i == 7:
                print("Engine")
                kbd.send(Keycode.UP_ARROW)
            if i == 11:
                print("Weapon")
                kbd.send(Keycode.RIGHT_ARROW)
            if i == 15:
                print("Reset")
                kbd.send(Keycode.DOWN_ARROW)
        if buttons[i].rose:
            print(" ")
