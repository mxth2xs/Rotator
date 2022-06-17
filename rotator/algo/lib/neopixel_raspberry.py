import board
import neopixel
from config import num_led
import rotator.algo.lib.neopixel_raspberry_pixelbuf as pixelbuf
# Configure the setup
PIXEL_PIN = board.D21  # pin that the NeoPixel is connected to
ORDER = neopixel.GRB  # pixel color channel order

# Create the NeoPixel object
led = neopixel.NeoPixel(PIXEL_PIN, num_led, brightness=0.2, auto_write=False, pixel_order=ORDER)

class NeoPixel_raspberry(pixelbuf.PixelBuf):
    def setPixelColor(self, pixel, red, green, blue):
        led[pixel] = (red, green, blue)