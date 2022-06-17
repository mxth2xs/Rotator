import board
import neopixel

# Configure the setup
PIXEL_PIN = board.D21  # pin that the NeoPixel is connected to
ORDER = neopixel.GRB  # pixel color channel order

# Create the NeoPixel object
led = neopixel.NeoPixel(PIXEL_PIN, 484, pixel_order=ORDER)

class NeoPixel_raspberry(object):
    def setPixelColor(self, pixel, red, green, blue):
        led[pixel] = (red, green, blue)