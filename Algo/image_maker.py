def image_maker(*args):
    global img,auto
    # +------------------- Imports -------------------+ #
    from PIL import Image
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    try:
        from lib.neopixel_arduino import NeoPixel_arduino
    except:
        from Algo.lib.neopixel_arduino import NeoPixel_arduino
    from random import choice
    from os import listdir
    from pathlib import Path
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
        if img.mode == 'RGBA':
            for color in range(len(liste_colors)):
                liste_colors[color] = liste_colors[color][:-1]
        # +-----------------------------------------------+ #
        
        # +--------------- Afficher l'image --------------+ #
        # - Afficher sur PC (optionnel)
        imgSmall.show()

        # - Afficher sur LEDs 
        for led in range(num_led):
            print(liste_colors)
            strand.setPixelColor(led, liste_colors[led][0], liste_colors[led][1], liste_colors[led][2])
            strand.show()
        # +-----------------------------------------------+ #

    def pixel_art(list_color):
        strand.show()
        for y in range(len(list_color)):
            for x in range(len(list_color[y])):
                
                if list_color[y][x][0] != "x":
                    strand.setPixelColor(int(list_color[y][x][0]), int(list_color[y][x][1]), int(list_color[y][x][2]), int(list_color[y][x][3]))
                    strand.show()

    # +---------------- Import d'image ---------------+ #
    if args[0] == False:
        Tk().withdraw()
        filename = askopenfilename()
        img = Image.open(filename)
        run_normal()
    elif args[0] == True:
        img = Image.open( Path(str(Path(__file__).parents[1] / 'images/random')+ "\\" +choice(listdir(Path(__file__).parents[1] / 'images/random'))))
        run_normal()
    elif args[0] == "death_snake":
        img = Image.open( Path(str(Path(__file__).parents[1] / 'images/death_snake')+ "\\" +choice(listdir(Path(__file__).parents[1] / 'images/death_snake'))))
        run_normal()
    elif args[0] == "scribble_creation":
        img = Image.open( Path(str(Path(__file__).parents[1] / 'images/scribble_creation')+ "\\" + "IMAGE-" + str(len(listdir(Path(__file__).parents[1] / 'images/scribble_creation'))) + ".jpg"))
        pixel_art(args[1])
    else:
        pass
    # +-----------------------------------------------+ #

if __name__ == "__main__":

    # +----------------- Config LEDs -----------------+ #
    try:
        from lib.neopixel_arduino import NeoPixel_arduino
    except:
        from Algo.lib.neopixel_arduino import NeoPixel_arduino

    strand = NeoPixel_arduino('COM3')
    num_led = 484
    strand.show()
    # +-----------------------------------------------+ #


    image_maker(False)