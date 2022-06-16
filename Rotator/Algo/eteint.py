#CE PROGRAMME A ETE CONCU POUR ETEINDRE L'ENTIERETE DU PANNEAU SANS PASSER PAR __MAIN__.py

def eteint(device):
    num_led = 484

    #--------------------------------------------- IMPORT DES LIBRAIRIES ARDUINO ---------------------------------------------
    if device == False:
        from lib.neopixel_arduino import NeoPixel_arduino
        NeoPixel = NeoPixel_arduino
        strand = NeoPixel('COM3') #Choisissez le port série où votre Arduino est connecté. Cette information est visible sur le logiciel Arduino IDE
        strand.show()


    #--------------------------------------------- PROGRAMME QUI ETEINT LES LEDS ---------------------------------------------
    for i in range(num_led):
        strand.setPixelColor(i, 0, 0 ,0)

    strand.show()

if __name__ == "__main__":
    eteint(False)