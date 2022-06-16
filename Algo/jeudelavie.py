def jeudelavie():
    global table
    import random
    try:
        from lib.neopixel_arduino import NeoPixel_arduino
    except:
        from Algo.lib.neopixel_arduino import NeoPixel_arduino
    from player import strand

    table=[]

    L= 60
    H= 20

    #Création d'un tableaux vierge
    def tableaux(L,H,table):
        for i in range(H):
            table.append([])
            for j in range(L):
                table[i].append(0)
        return table

    #Remplissage de ce tableau par un tableau de départ aléatoire 
    def aléatoire(table): 
        for i in range (0,H):
            for y in range (0,L):
                table[i][y]=random.randint(0,1)
        return table


    #Calcule le nombre de cases "vivantes" autours d'une certaine case et les comptabilise
    def calculautour(x,y,H,L,table): 
        autour=0
        for xi in range (x-1,x+1): 
            for yi in range (y-1,y+1):
                if table[xi%H][yi]>0 :
                    autour+=1
                else:
                    None
        return autour

        
    def globalcalcul(L,H,table):
        around=[]
        for x in range (H):
            around.append([])
            for y in range (L):
                around[x].append(calculautour(x,y,H,L,table))

        for x in range (H):
            for y in range (L):
                if around[x][y]==2 and table[x][y]>0:
                    None
                elif around[x][y]==3 and table[x][y]>0:
                    None
                elif around[x][y]==3 and table[x][y]==0:
                    table[x][y]=1
                else:
                    table[x][y]=0
        return table

    #Création d'une boucle répétition qui force la répétition du programme "rep" nombre de fois
    def boucle(table,rep):
        while rep>=0:
            globalcalcul(L, H,table)
            allumer_leds(table)
            rep-=1

    #Lecture de la liste table afin d'allumer les leds
    def allumer_leds(table):
        for i in range (len(table)):
            for j in range (22):
                if i%2==0:
                    if table[i][j]==0:
                        strand.setPixelColor(22*i+j, 0,0,0)
                    elif table[i][j]==1:
                        strand.setPixelColor(22*i+j, 255,0,0)
                else:
                    if table[i][j]==0:
                        strand.setPixelColor(22*(i+1)-j, 0,0,0)
                    elif table[i][j]==1:
                        strand.setPixelColor(22*(i+1)-j, 255,0,0)
        strand.show()

    tableaux(L,H,table)
    aléatoire(table)
    boucle(table,800)

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

    jeudelavie()