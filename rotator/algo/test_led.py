def test_led():
    import time
    from rotator.config import strand, num_led, width, height

    Time = 0.001
    while True:
        for i in range (num_led-1):
            strand.setPixelColor(i, 255, 0, 0)
        
        strand.show()
        time.sleep(5)
        strand.show()

        for i in range(num_led-1):
            strand.setPixelColor(i, 255, 0, 0)
            time.sleep(Time)
            strand.setPixelColor(i+1, 255, 0, 0)
            time.sleep(Time)
            strand.show()
            strand.setPixelColor(i, 0, 0, 0)
            time.sleep(Time)
            strand.setPixelColor(i+1, 0, 0, 0)
            time.sleep(Time)
            strand.show()
            if num_led == 484:
                strand.setPixelColor(483, 255, 0, 0)
                strand.setPixelColor(482, 255, 0, 0)
                time.sleep(3)
                strand.show()
            elif num_led == 968:
                strand.setPixelColor(483, 255, 0, 0)
                strand.setPixelColor(482, 255, 0, 0)
                strand.setPixelColor(967, 255, 0, 0)
                strand.setPixelColor(466, 255, 0, 0)
                time.sleep(5)
                strand.show()


if __name__ == "__main__":
    test_led()