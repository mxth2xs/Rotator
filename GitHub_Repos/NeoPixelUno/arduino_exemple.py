import neopixel
import time

strand = neopixel.NeoPixel('/dev/ttyACM0')
for x in range(5):
    strand.setPixelColor(x, 255, 0, 0)
    strand.show()
    time.sleep(1)
    strand.setPixelColor(x, 0, 255, 0)
    strand.show()
    time.sleep(1)
    strand.setPixelColor(x, 0, 0, 255)
    strand.show()
    time.sleep(1)

