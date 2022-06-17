from turtle import delay


def test_led():
    import time
    from config import strand, num_led, width, height

    """while True:
        for i in range(num_led):
            strand.setPixelColor(i, 255, 0, 0)
            time.sleep(0.01)
            strand.setPixelColor(i, 0, 0, 0)
            time.sleep(0.01)"""

    strand.setPixelColor(968, 255, 0, 0)

if __name__ == "__main__":
    test_led()