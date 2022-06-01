def scribble():
    import tkinter as tk
    from tkinter.colorchooser import askcolor
    from PIL import ImageGrab,Image
    from os import listdir
    from pathlib import Path
    import image_maker

    #Lancement de la fenêtre Canvas
    scribble = tk.Tk()
    C = tk.Canvas(scribble, bg="white", height=440+20, width=440)
    image = False

    def change_color():
        global colors
        colors = askcolor(title="Tkinter Color Chooser")
        scribble.configure(bg=colors[1])


    tk.Button(scribble, text='Choisir une couleur', command=change_color).grid(row=0, column=0)

    def left_click(event):
        global X,Y, colors, bandeau,click
        click = True
        X = event.x
        Y = event.y
        
        recup_coord()
        if bandeau == True:
            carre = C.create_rectangle(coord, fill = colors[1], outline="")

    def right_click(event):
        global X,Y,colors, bandeau 
        X = event.x
        Y = event.y
        colors = "#ffffff"

        recup_coord()
        if bandeau == True:
            carre = C.create_rectangle(coord, fill = colors, outline="")

    scribble.bind('<B1-Motion>',left_click)
    scribble.bind('<B3-Motion>',right_click)

    def recup_coord():
        global X,Y,coord, bandeau
        if X//20 == 0 or Y//20 == 0:
            if X//20 == 0 and Y//20 == 0:
                X+=1
                Y+=1
            elif X//20 == 0:
                X+=1
            else:
                Y+=1

        if Y <= 20:
            bandeau = False
        else:
            bandeau = True

        x1_final = (X//20)*20
        y1_final = (Y//20)*20
        x2_final = (X//20)*20+20
        y2_final = (Y//20)*20+20
        coord = x1_final, y1_final, x2_final, y2_final


    def export_image():
        global img,image
        x = C.winfo_rootx()
        y = C.winfo_rooty()
        w = C.winfo_width()
        h = C.winfo_height()
        img= ImageGrab.grab((x, y, x+w, y+h)).save("images/scribble_creation/IMAGE-"+ str(len(listdir(Path(__file__).parents[1] / 'images/scribble_creation'))+1) +".png")
        image = True
        
    
    def print_image():
        if image == True:
            


    tk.Button(scribble, text='Exporter image', command=export_image).grid(row = 0, column=1)
    tk.Button(scribble, text='Afficher image sur les leds', command=print_image).grid(row = 0, column=1)


    #Affichage de la fenêtre Canvas
    C.grid(row=1, column=0, columnspan=2)
    scribble.mainloop()


scribble() 