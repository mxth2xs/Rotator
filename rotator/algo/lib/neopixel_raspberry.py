import board
import neopixel
from config import num_led

# Configure the setup
PIXEL_PIN = board.D21  # pin that the NeoPixel is connected to
ORDER = neopixel.GRB  # pixel color channel order

# Create the NeoPixel object
led = neopixel.NeoPixel(PIXEL_PIN, num_led, pixel_order=ORDER)

class NeoPixel_raspberry(object):
    def setPixelColor(self, pixel, red, green, blue):
        led[pixel] = (red, green, blue)