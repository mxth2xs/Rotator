def eteint():

    from lib.neopixel_arduino import NeoPixel

    #Script pour la configuration des LEDs.
    strand = NeoPixel('COM3')
    strand.show()

if __name__ == "__main__":
    eteint()