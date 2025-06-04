# src/drivers/prox_trinkey.py

import board
import neopixel
from adafruit_apds9960.apds9960 import APDS9960
import touchio
from src.abstract import ProximitySensor, LEDController, TouchSensor

class _ProxSensor(ProximitySensor):
    """Wraps APDS9960 to implement ProximitySensor on the Proximity Trinkey."""
    def __init__(self, i2c_bus):
        self._apds = APDS9960(i2c_bus)
        self._apds.enable_proximity = True

    @property
    def proximity(self) -> int:
        return self._apds.proximity

class _LEDs(LEDController):
    """Wraps the two onboard NeoPixels to implement LEDController."""
    def __init__(self, brightness: float = 0.1):
        self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 2, brightness=brightness)

    def fill(self, color: tuple[int, int, int]) -> None:
        self._pixels.fill(color)

class _TouchPad(TouchSensor):
    """Wraps the capacitive TOUCH2 pin for TouchSensor."""
    def __init__(self):
        self._touch = touchio.TouchIn(board.TOUCH2)

    @property
    def value(self) -> bool:
        return self._touch.value

def make_prox_trinkey_devices(i2c_bus):
    """
    Returns (ProxSensor, LEDs, TouchPad) as concrete implementations of
    (ProximitySensor, LEDController, TouchSensor).
    Usage:
        i2c = board.I2C()
        apds, pixels, touch = make_prox_trinkey_devices(i2c)
    """
    apds = _ProxSensor(i2c_bus)
    pixels = _LEDs()
    touch = _TouchPad()
    return apds, pixels, touch
