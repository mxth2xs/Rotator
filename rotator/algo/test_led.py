def test_led():
    import time
    from config import strand, num_led, width, height

    while True:
        for i in range(num_led-1):
            strand.setPixelColor(i, 255, 0, 0)
            time.sleep(0.001)
            strand.setPixelColor(i+1, 255, 0, 0)
            time.sleep(0.001)
            strand.show()
            strand.setPixelColor(i, 0, 0, 0)
            time.sleep(0.001)
            strand.setPixelColor(i+1, 0, 0, 0)
            time.sleep(0.001)
            strand.show()
            

    """while True:
        strand.setPixelColor(483, 255, 0, 0)
        strand.setPixelColor(482, 255, 0, 0)"""

if __name__ == "__main__":
    test_led()