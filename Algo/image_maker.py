def image_maker(auto = False):
    # +------------------- Imports -------------------+ #
    from PIL import Image
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    try:
        from lib.neopixel import NeoPixel
    except:
        from Algo.lib.neopixel import NeoPixel
    from random import choice
    from os import listdir
    from pathlib import Path
    # +-----------------------------------------------+ #

	# +----------------- Config LEDs -----------------+ #
    strand = NeoPixel('COM3')
    num_led = 484
    # +-----------------------------------------------+ #

    # +---------------- Import d'image ---------------+ #
    if auto == False:
        Tk().withdraw()
        filename = askopenfilename()
        img = Image.open(filename)
    elif auto == True:
        img = Image.open( Path(str(Path(__file__).parents[1] / 'images')+ "\\" +choice(listdir(Path(__file__).parents[1] / 'images'))))
    elif auto == "death_snake":
        img = Image.open( Path(str(Path(__file__).parents[1] / 'death_snake')+ "\\" +choice(listdir(Path(__file__).parents[1] / 'death_snake'))))
    else:
        pass
    # +-----------------------------------------------+ #

    # +-------- Redimension de l'image (22x22) -------+ #
    # - Si l'image a déjà les bonnes dimensions, on demande directement la liste de couleurs.
    if img.size == (22,22):
        liste_colors = list(img.getdata())
        imgSmall = img
    
    # - Sinon, on redimensionne et on demande la liste...
    else:
        imgSmall = img.resize((22,22),resample=Image.NEAREST)    
        liste_colors = list(imgSmall.getdata())

    #- Enlever la valeur de la transparence si 'png' (RGBA -> RGB).
    if img.format.lower() == 'png':
        for color in range(len(liste_colors)):
            liste_colors[color] = liste_colors[color][:-1] 
    # +-----------------------------------------------+ #
    
    # +--------------- Afficher l'image --------------+ #
    # - Afficher sur PC (optionnel)
    imgSmall.show()

    # - Afficher sur LEDs   
    for led in range(num_led):
        strand.setPixelColor(led, liste_colors[led][0], liste_colors[led][1], liste_colors[led][2])
        strand.show()
    # +-----------------------------------------------+ #

if __name__ == "__main__":
    image_maker(True)