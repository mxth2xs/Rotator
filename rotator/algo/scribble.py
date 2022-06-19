def scribble():
    global colors, image

    import tkinter as tk
    from tkinter.colorchooser import askcolor
    from PIL import ImageGrab,Image,ImageColor
    from os import listdir,remove
    from rotator.algo.image_maker import image_maker 
    import random
    try:
        from rotator.config import height_screen, width_screen, width, height
    except:
        height_screen, width_screen, height, width = 1080, 1920, 44, 22
    
    taille_grille = 20
    image = False

    #Lancement de la fenêtre Canvas
    scribble = tk.Tk()
    C = tk.Canvas(scribble, bg="black", width=width*taille_grille, height=height*taille_grille)
    
    colors = ((0, 0, 0), "#000000")

    #Création de la liste de couleur vide + création de la grille de fond
    def list_color_creation():
        global list_color
        list_color = []
    
        for y in range(height):
            list_color.append([])
            for x in range(width):
                list_color[y].append(["x", "r", "g", "b", C.create_rectangle(x*taille_grille, y*taille_grille, x*taille_grille+taille_grille, y*taille_grille+taille_grille, fill = "#000000", outline="#FFFF00")])
        C.grid(row=1, column=0, columnspan=4)
                
        return list_color
    
    list_color_creation()

    #Bouton pour changer de couleur
    def change_color():
        global colors
        colors = askcolor(title="Tkinter Color Chooser")
        scribble.configure(bg=colors[1])

    tk.Button(scribble, text='Choisir une couleur', command=change_color).grid(row=0, column=0)

    #Bouton pour exporter l'image
    def export_image():
        global img,image
        x = C.winfo_rootx()
        y = C.winfo_rooty()
        w = C.winfo_width()
        h = C.winfo_height()
        img= ImageGrab.grab((x, y, x+w, y+h)).save("rotator/images/scribble_creation/IMAGE-"+ str(len(listdir('rotator/images/scribble_creation'))+1) +".png")
        image = True
    
    #Bouton pour afficher l'image (utilisation du module image_maker)
    def print_image():
        global image
        if image == True:
            image_maker("scribble_creation", list_color)
            image = False

        else:
            x = C.winfo_rootx()
            y = C.winfo_rooty()
            w = C.winfo_width()
            h = C.winfo_height()
            img= ImageGrab.grab((x, y, x+w, y+h)).save("rotator/images/scribble_creation/IMAGE-"+ str(len(listdir('rotator/images/scribble_creation')+1) +".jpg"))
            image_maker("scribble_creation", list_color)
            remove("images/scribble_creation/IMAGE-"+ str(len(listdir(listdir('rotator/images/scribble_creation'))+1) +".jpg"))

    #Recommencer le dessin
    def destroy():
        C.delete('all')
        list_color_creation()

    tk.Button(scribble, text='Exporter image_pixel', command=export_image).grid(row = 0, column=1)
    tk.Button(scribble, text='Afficher image_pixel sur les leds', command=print_image).grid(row = 0, column=2)
    tk.Button(scribble, text='Supprimer dessin', command=destroy).grid(row = 0, column=3)

    def click(event, couleur):
        global X,Y, list_color
        X = event.x
        Y = event.y
        if X >=0 and Y >= 0 and X < width*taille_grille and Y < height*taille_grille:
            C.itemconfig(list_color[Y//taille_grille][X//taille_grille][4], fill = couleur)

            if Y//taille_grille%2 == 0:
                led = list_color[Y//taille_grille][X//taille_grille][4]-1

            else:
                led = (Y//taille_grille+1)*(width-1)+Y//taille_grille-X//taille_grille

            list_color[Y//taille_grille][X//taille_grille][0] = led
            list_color[Y//taille_grille][X//taille_grille][1] = colors[0][0]
            list_color[Y//taille_grille][X//taille_grille][2] = colors[0][1]
            list_color[Y//taille_grille][X//taille_grille][3] = colors[0][2]

    
    scribble.bind('<B1-Motion>',lambda event: click(event, colors[1]))
    scribble.bind('<Button-1>',lambda event: click(event, colors[1]))
    scribble.bind('<B2-Motion>',lambda event: click(event, "#"+"".join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'], 6))))
    scribble.bind('<Button-2>',lambda event: click(event, "#"+"".join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'], 6))))
    scribble.bind('<B3-Motion>',lambda event: click(event, '#000000'))
    scribble.bind('<Button-3>',lambda event: click(event, '#000000'))
    
    
    scribble.mainloop()
    #Affichage de la fenêtre Canvas
    

if __name__ == "__main__":
    scribble()