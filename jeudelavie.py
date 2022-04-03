# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 10:55:46 2022

@author: cades
"""
table=[]

def calculautour(x,y,H,L): #calcule le nombre de cases "vivantes" autours d'une certaine case et les comptabilise
    global table, around
    autour=0
    for xi in range (x-1,x+2): 
        for yi in range (y-1,y+2):
            if xi==x and yi==y:
                None 
            elif xi<0 or yi<0:
                None
            elif xi>=H or yi>=L:
                None
            elif table[xi][yi]>0 :
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
    print(around)
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

def tableaux (L,H):
    table=[]
    for i in range (0,H):
        ligne=[]
        for y in range (0,L):
            ligne.append(0)
        table.append(ligne)
    return table

def addvalue (x,y,a):
    global table
    table[x][y]=a
    
L=5
H= 10
table=tableaux(L, H)
print (table, "tableau vierge")
addvalue(1, 1, 1)
addvalue(1, 2, 1)
addvalue(1, 3, 1)
print(table, "une fois configuré")
globalcalcul(L, H)
print(table, "après un tour")
