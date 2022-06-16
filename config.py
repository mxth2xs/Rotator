"""
Ceci est un fichier de configuration. 
Suivez les étapes du fichier README.md afin de régler les paramètres au plus proche de vos besoins.
"""
from Algo.lib.neopixel_arduino import NeoPixel_arduino
from Algo.lib.neopixel_raspberry import NeoPixel_raspberry

#Choisissez votre appareil: ARDUINO = False, RASPBERRY = True

device = False


#CONFIGURATION DU PROGRAMME POUR UN ARDUINO
if device == False:
    neopixel = NeoPixel_arduino


#CONFIGURATION DU PROGRAMME POUR UN RASPBERRY
if device == True:
    neopixel = NeoPixel_raspberry