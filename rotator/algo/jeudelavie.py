#EN COURS DE RECODAGE COMPLET

def jeudelavie(pattern = "aleatoire"):
    import random
    try:
        from rotator.config import height_screen, width_screen, width, height
    except:
        height_screen, width_screen, height, width = 1080, 1920, 44, 22    

    #Création de la liste de départ vide
    def list_life_creation():
        global list_life
        list_life = []
        for y in range(height):
            list_life.append([])
            for x in range(width):
                list_life[y].append(["x", "r", "g", "b"])          
        return list_life   
    
    list_life_creation()

    def list_life_creation_intermediaire():
        global list_life_intermediaire
        list_life_intermediaire = []
        for y in range(height):
            list_life_intermediaire.append([])
            for x in range(width):
                list_life_intermediaire[y].append(["x", "r", "g", "b"])          
        return list_life_intermediaire   

    def calcul_autour():
        for y in range(height):
            for x in range(width):
                somme = 0
                #Les coins
                if list_life[y][x][3] == 255 and : #Coin haut-gauche
                
                if list_life[y][x][3] == 255 and : #Coin haut-droite

                if list_life[y][x][3] == 255 and : #Coin bas-gauche

                if list_life[y][x][3] == 255 and : #Coin bas-droite

                #Les bords
                if list_life[y][x][3] == 255 and : #

    if pattern == "aleatoire":
        #------------------------ Création du pattern de départ, avec au hasard led allumée ou non, pour diminuer l'occurence de led allumé, deux if random.choice...
        for y in range(height):
            for x in range(width):

                if y%2 == 0:
                    led = y*(width-1)+x+y

                else:
                    led = (y+1)*(width-1)+y-x
                
                if random.choice([True, False]):
                    if random.choice([True, False]):
                        list_life[y][x][0], list_life[y][x][1], list_life[y][x][2], list_life[y][x][3] = led, 0, 0, 255

                    else:
                        list_life[y][x][0], list_life[y][x][1], list_life[y][x][2], list_life[y][x][3] = led, 0, 0, 0
                    
                else:
                    list_life[y][x][0], list_life[y][x][1], list_life[y][x][2], list_life[y][x][3] = led, 0, 0, 0
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif pattern == "scribble":
        pass

if __name__ == "__main__":
    jeudelavie()