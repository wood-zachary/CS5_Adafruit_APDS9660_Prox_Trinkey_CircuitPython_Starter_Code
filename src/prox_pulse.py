# import time

from .pulse import pulse
from .abstract import LEDController, ProximitySensor
from support.mytyping import NoReturn

THRESHOLD: int = 75

RED: tuple[int, int, int] = (150, 10, 10)
GREEN: tuple[int, int, int] = (30, 100, 10)


def prox_pulse(px: LEDController, color: tuple[int, int, int], prox: int) -> None:
    """
    Maps proximity value to pulse duration and calls pulse.

    Args:
        px: LED controller object.
        color (tuple): color to pulse.
        prox (int): proximity value.
    """
    ### Your Code Here!


def run_prox_pulse(apds: ProximitySensor, pixels: LEDController) -> NoReturn:
    """
    Runs proximity-based pulsing demo.

    Args:
        apds: proximity sensor.
        pixels: LED controller object.
    """
    # Main loop
    while True:
        if apds.proximity >= THRESHOLD:
            pulse(pixels, RED, 0.3)
            # prox_pulse(pixels, RED, apds.proximity)
        else: 
            pulse(pixels, GREEN, 0.3)
            # prox_pulse(pixels, GREEN, apds.proximity)
