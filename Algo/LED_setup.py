def LED_setup():
    # +-------------- Setup LEDs --------------+ #    
    import board, neopixel

    pixel_pin = board.D18
    num_pixels = 22*22
    ORDER = neopixel.RGB
    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
    )
    # +----------------------------------------+ #
    return num_pixels, pixels