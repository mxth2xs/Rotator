def image_maker(auto = False):
    global img
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

    def run_normal():
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

    def pixel_art(list_color):
        for x in range(len(list_color)):
            for y in range(list_color[x]):
               

                strand.setPixelColor(X, rgb[0], rgb[1], rgb[2])
                strand.show()

    # +---------------- Import d'image ---------------+ #
    if auto == False:
        Tk().withdraw()
        filename = askopenfilename()
        img = Image.open(filename)
        run_normal()
    elif auto == True:
        img = Image.open( Path(str(Path(__file__).parents[1] / 'images')+ "\\" +choice(listdir(Path(__file__).parents[1] / 'images'))))
        run_normal()
    elif auto == "death_snake":
        img = Image.open( Path(str(Path(__file__).parents[1] / 'images/death_snake')+ "\\" +choice(listdir(Path(__file__).parents[1] / 'images/death_snake'))))
        run_normal()
    elif auto == "scribble_creation":
        img = Image.open( Path(str(Path(__file__).parents[1] / 'images/scribble_creation')+ "\\" + "IMAGE-" + str(len(listdir(Path(__file__).parents[1] / 'images/scribble_creation'))) + ".jpg"))
        pixel_art(list_color)
    else:
        pass
    # +-----------------------------------------------+ #

if __name__ == "__main__":
    image_maker(True)