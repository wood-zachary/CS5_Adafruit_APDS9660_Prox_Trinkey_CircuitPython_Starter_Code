from .abstract import LEDController, ProximitySensor, TouchSensor
from .pulse import run_simple_pulse
# from .prox_pulse import run_prox_pulse
# from .morse_engine import run_morse_engine
# from .macros import run_macros

'''
Always comment out any imports you're not using to save memory. The APDS9660 board has very little memory!
'''

def run(apds: ProximitySensor, pixels: LEDController, touch: TouchSensor):
    """
    Runs the selected demo on the Trinkey.

    Args:
        apds: proximity sensor.
        pixels: LED controller object.
        touch: touch sensor.
    """
    run_simple_pulse(pixels)
    # run_prox_pulse(apds, pixels)
    # run_morse_engine(apds, pixels, touch)
    # run_macros(apds, pixels)
