try:
    import board
except ModuleNotFoundError:
    pass
else:
    from src.drivers.prox_trinkey import make_prox_trinkey_devices
    from src.interact import run

    i2c = board.I2C()
    apds, pixels, touch = make_prox_trinkey_devices(i2c)
    print("Loaded Prox Trinkey…")

    run(apds, pixels, touch)
