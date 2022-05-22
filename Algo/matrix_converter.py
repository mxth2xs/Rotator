#Fonction pour allumer les LEDs entrées sous forme de coordonnées.
def allumer_LEDs(pixels, matrix):
    """
    pixels: liste donnée par neopixel...
    matrix: liste contenant les coordonnées de LEDs à allumer et leur couleur (matrix = [[x,y,(R,G,B)], ...]]).
    """
    
    # Pour les tests sans board.
    #pixels = [(0,0,0) for i in range(22*22)]
    ###########################

    #Pour chaque LED dans la liste donnée, 
    for led in matrix:
        # - Transformer ses coordonnées en numéro,
        # - Ajouter la couleur associée dans la liste des pixels au pixel du numéro obtenu
        pixels[(led[0]*22)+led[1]] = led[2]
    
    #Afficher les pixels !
    #pixels.show()
    
    return pixels
