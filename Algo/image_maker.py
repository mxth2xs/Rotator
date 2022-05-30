def image_maker():
    # +------------------- Imports -------------------+ #
    from PIL import Image
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    from lib.neopixel import NeoPixel
    # +-----------------------------------------------+ #

	# +----------------- Config LEDs -----------------+ #
    strand = NeoPixel('COM3')
    num_led = 484
    # +-----------------------------------------------+ #

    # +---------------- Import d'image ---------------+ #
    Tk().withdraw()
    filename = askopenfilename()
    img = Image.open(filename)
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
    image_maker()