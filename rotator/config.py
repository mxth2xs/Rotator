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


#CONFIGURATION DU PROGRAMME POUR UN ARDUINO
if device == False:
    from rotator.algo.lib.neopixel_arduino import NeoPixel_arduino
    NeoPixel = NeoPixel_arduino
    strand = NeoPixel('COM3') #Choisissez le port série où votre Arduino est connecté. Cette information est visible sur le logiciel Arduino IDE
    strand.show()


#CONFIGURATION DU PROGRAMME POUR UN RASPBERRY
if device == True:
    from rotator.algo.lib.neopixel_raspberry import NeoPixel_raspberry
    strand = NeoPixel_raspberry()