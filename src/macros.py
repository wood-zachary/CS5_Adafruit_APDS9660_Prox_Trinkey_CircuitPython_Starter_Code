from .abstract import LEDController, ProximitySensor 
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode 
# from adafruit_hid.consumer_control import ConsumerControl
# from adafruit_hid.consumer_control_code import ConsumerControlCode 
# from adafruit_hid.mouse import Mouse
from support.mytyping import NoReturn

def run_macros(apds: ProximitySensor, pixels: LEDController) -> NoReturn:
    THRESHOLD = 3
    DURATION = 0.25
    INTERVAL = 0.05
    GREEN = ((0, 150, 0))
    YELLOW = ((75, 75, 0))

    kb_macro = Keycode.SPACE

    kb = Keyboard(usb_hid.devices) 
    # cc = ConsumerControl(usb_hid.devices)
    # ms = Mouse(usb_hid.devices)
    pixels.fill(YELLOW)
    
    last_prox = 0
    
    while True:
        prox = apds.proximity

        if prox > THRESHOLD and last_prox <= THRESHOLD:
            ...
            ### Your Code Here!
        
        last_prox = prox

        time.sleep(INTERVAL)