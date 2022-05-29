#!/bin/bash

sudo python3 -m pip install adafruit-circuitpython-neopixel
sudo python3 -m pip install board
sudo python3 -m pip install neopixel

mkdir ~/github/ && cd ~/github/
git clone https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel.git
cd ./Adafruit_CircuitPython_NeoPixel/examples/
sudo python3 ./neopixel_rpi_simpletest.py
