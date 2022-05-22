# Simple startup animation for the Rotator project.

# +----- Import libs -----+ #
import time
import board
import neopixel
# +-----------------------+ #


# +----- Setup -----+ #
# board pin
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 22*22 #22*22 = 484 || 22*44 = 968

# The order of the pixel colors (RGB or GRB)
ORDER = neopixel.RGB


pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
# +------------------+ #


# +----- Color constants -----+ #
RED=(255,0,0)
BLUE=(0,255,0)
GREEN=(0,0,255)
WHITE=(255,255,255)
CLEAR=(0,0,0)
# +---------------------------+ #


# +----- Make the snake board a grid of two dimentions -----+ #

def matrix():
    matrix = []
    for i in range(num_pixels//22):
        matrix.append(["+" for j in range(22)])
    print(matrix)

def printed_matrix(matrix):
    printed_matrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            printed_matrix += matrix[i][j] + " "
        printed_matrix += "\n"
    return printed_matrix
# +---------------------------------------------------------+ #




# +----- Animaion -----+ #
"""
while True:
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

    pixels.fill((0, 0, 255))
    pixels.show()
    time.sleep(1)
"""
    

for i in matrix:
    i[-1] = "0"
    i[0] = "0"
    print(i)

print()
for a in range(len(matrix[0])):
    matrix[0][a] = '0'
    matrix[-1][a] = '0'

print(printed_matrix(matrix))

