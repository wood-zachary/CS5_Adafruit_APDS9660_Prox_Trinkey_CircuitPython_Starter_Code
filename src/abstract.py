"""Collection of abstract classes for type hinting in the rest of the project.

(For students: don't worry about the code that's in here.
These classes are just providing examples of how to use the sensors
and other peripherals for type hinting.
The actual implementations of the classes are on the device.)
"""
# We aren't using the abc module because it isn't available on circuitpy.

class ProximitySensor:
    """Abstract proximity sensor."""

    @property
    def proximity(self) -> int:
        """Integer in [0, 255] indicating proximity of object to sensor.

        Lower is farther away and higher is closer.

        Example:
            `apds.proximity`
        """
        raise NotImplementedError


class LEDController:
    """Abstract LED controller."""

    def fill(self, color: tuple[int, int, int]) -> None:
        """Change the color of the LED being controlled.

        Args:
            color: Three-tuple of integers in [0, 255] representing the values
                of red, green, and blue to display on the LED.

        Example:
            `px.fill((0, 0, 0))` turns the LED off
        """
        raise NotImplementedError


class TouchSensor:
    """Abstract touch sensor."""

    @property
    def value(self) -> bool:
        """If the sensor is being touched.

        Example:
            `touch.value`
        """
        raise NotImplementedError