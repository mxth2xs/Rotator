#!/usr/bin/python
import struct
import serial
import time

class NeoPixel_arduino(object):
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(self.port, 115200, timeout=60)
        self.command_count = 0

    def setPixelColor(self, pixel, red, green, blue):
        message = struct.pack('>BBBHBBB', ord(':'), self.command_count, ord('c'), pixel, red, green, blue)
        self.command_count += 1
        if self.command_count >=255:
            self.command_count = 0
        #print(message)
        self.ser.write(message)
        response = self.ser.readline()
        #print(response)

    def show(self):
        message = struct.pack('BBB', ord(':'), self.command_count, ord('s'))
        self.command_count += 1
        #print(message)
        self.ser.write(message)
        response = self.ser.readline()
        #print(response)

    def fillPixels(strand, red, green, blue):
        for i in range(484):
            strand.setPixelColor(i, red, green, blue)


if __name__ == "__main__":

    strand = NeoPixel_arduino('COM3')

    for i in range(484):
        strand.setPixelColor(i, 255, 0, 0)

    strand.show()