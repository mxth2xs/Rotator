# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 10:55:46 2022

@author: cades
"""
import random,neopixel,board
import neopixel


#LED setup
pixel_pin = board.D18
num_pixels = 22*22
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


table=[]

def allumer_leds():
    global table
    for i in range (len(table)):
        for j in range (22):
            if i%2==0:
                if table[i][j]==0:
                    pixels[22*i+j]=(0,0,0)
                elif table[i][j]==1:
                    pixels[22*i+j]=(255,0,0)
                elif table[i][j]==2:
                    pixels[22*i+j]=(0,255,0)
            else:
                if table[i][j]==0:
                    pixels[22*(i+1)-j]=(0,0,0)
                elif table[i][j]==1:
                    pixels[22*(i+1)-j]=(255,0,0)
                elif table[i][j]==2:
                    pixels[22*(i+1)-j]=(0,255,0)

    pixels.show()

def calculautour(x,y,H,L): #calcule le nombre de cases "vivantes" autours d'une certaine case et les comptabilise
    global table, around
    autour=0
    for xi in range (x-1,x+2): 
        for yi in range (y-1,y+2):
            if xi==x and yi==y:
                None 
            elif yi<0:
                None
            elif yi>=L:
                None
            elif table[xi%H][yi]>0 :
                  autour+=1
                 # print(x,y,xi,yi)
            else:
                None
    return autour

    
def globalcalcul (L,H):
    global table
    around=[]
    for x in range (H):
        ligne=[]
        for y in range (L):
            ligne.append(calculautour(x,y,H,L))
        around.append(ligne)
    #print(around)
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

def tableaux (L,H):#création d'un tableaux vierge
    table=[]
    for i in range (0,H):
        ligne=[]
        for y in range (0,L):
            ligne.append(0)
        table.append(ligne)
    return table

"""def addvalue (x,y,a): # pour ajouter une valeur
    global table
    table[x][y]=a"""

def boucle(tab,time,rep):
    tt=0
    global table
    while rep>=0:
        for i in range (0,1000000*time):
            tt=tt
        globalcalcul(L, H)
        allumer_leds()
        rep-=1
        #tablo()
        #print(tablo())
        #print("-----------------------------------------------------")

def aléatoire(): #création d'un tableaux aléatoire
    global table
    for i in range (0,H):
        for y in range (0,L):
            table[i][y]=random.randint(0,1)
    return table

"""def tablo():
    global table
    tableau_bo = ""
    for i in table:
        for j in i:
            if j==0:
                tableau_bo = tableau_bo + " " + " "
            else:
                tableau_bo = tableau_bo + str(j) + " "
        tableau_bo += "\n"   
    return tableau_bo"""
 

"""print (tablo, "tableau vierge")
aléatoire()
print(tablo())
globalcalcul(L, H)
print("initial")
print(tablo(), "après un tour")
boucle(table,10,800)"""


table
L=60
H= 20
table=tableaux(L, H)
aléatoire()
boucle(table,10,800)
