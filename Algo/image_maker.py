def image_maker():
    from PIL import Image
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    from .lib.neopixel import NeoPixel

    #Script pour la configuration des LEDs.
    strand = NeoPixel('COM3')
    num_led = 484
  
    #Import d'image
    Tk().withdraw()
    filename = askopenfilename()
    img = Image.open(filename)


    if img.size == (22,22):
        #récupérer les couleurs des pixels (liste de tuples)
        pixels_origin = list(img.getdata())
        imgSmall = img

    else:
        # Changer les dimensions à 22x22
        imgSmall = img.resize((22,22),resample=Image.NEAREST)    
        pixels_origin = list(imgSmall.getdata())

        #Enlever la valeur de la transparence si le fichier est transparent.
        if img.format.lower() == 'png':
            for color in range(len(pixels_origin)):
                pixels_origin[color] = pixels_origin[color][:-1] 

    imgSmall.show()

    #Afficher   
    for led in range(num_led):
        strand.setPixelColor(led, pixels_origin[led][0], pixels_origin[led][1], pixels_origin[led][2])
        strand.show()
