"""
Ceci est un fichier de configuration. 
Suivez les étapes du fichier README.md afin de régler les paramètres au plus proche de vos besoins.
"""


#Choisissez votre appareil: ARDUINO = False, RASPBERRY = True

device = True

#Choisissez la taille de votre panneau, ici, c'est un carré de 22*22
height = 22
width = 22
num_led = height*width

#Choisissez la taille de l'écran
height_screen = 1920
width_screen = 1080


#CONFIGURATION DU PROGRAMME POUR UN ARDUINO
if device == False:
    from rotator.algo.lib.neopixel_arduino import NeoPixel_arduino
    NeoPixel = NeoPixel_arduino
    strand = NeoPixel('COM3') #Choisissez le port série où votre Arduino est connecté. Cette information est visible sur le logiciel Arduino IDE
    strand.show()


#CONFIGURATION DU PROGRAMME POUR UN RASPBERRY
if device == True:
    from rotator.algo.lib.neopixel_raspberry import NeoPixel_raspberry
    import board
    import neopixel as neopixel
    PIXEL_PIN = board.D21  # pin that the NeoPixel is connected to
    ORDER = neopixel.GRB  # pixel color channel order
    strand = NeoPixel_raspberry(PIXEL_PIN, num_led, brightness=0.2, auto_write=False, pixel_order=ORDER)