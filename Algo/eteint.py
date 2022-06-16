def eteint():

    from lib.neopixel_arduino import NeoPixel_arduino

    #Script pour la configuration des LEDs.
    strand = NeoPixel_arduino('COM3')
    strand.show()

if __name__ == "__main__":
    eteint()