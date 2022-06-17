from turtle import delay


def test_led():
    import time
    from config import strand, num_led, width, height

    while True:
        strand.setPixelColor(0, 255, 0, 0)
        time.sleep(0.5)
        strand.setPixelColor(0, 0, 0, 0)
        time.sleep(0.5)


if __name__ == "__main__":
    test_led()