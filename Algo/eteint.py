def eteint():

    from lib.neopixel import NeoPixel

    #Script pour la configuration des LEDs.
    strand = NeoPixel('COM3')
    num_led = 484
    strand.show()

eteint()