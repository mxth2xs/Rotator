def scribble():
    import tkinter as tk
    from tkinter.colorchooser import askcolor
    from PIL import ImageGrab,Image,ImageColor
    from os import listdir,remove
    from pathlib import Path
    from image_maker import image_maker

    #Lancement de la fenêtre Canvas
    scribble = tk.Tk()
    C = tk.Canvas(scribble, bg="black", height=460, width=440)
    image_pixel = False

    def change_color():
        global colors_rgb, colors
        colors = askcolor(title="Tkinter Color Chooser")
        scribble.configure(bg=colors[1])
        colors_rgb = ImageColor.getcolor(colors[1], "RGB")

    tk.Button(scribble, text='Choisir une couleur', command=change_color).grid(row=0, column=0)

    def list_color_creation():
        global list_color

        list_color = []
    
        for i in range(22):
            list_color.append([])
            for j in range(22):
                list_color[i].append(["x", "r", "g", "b"])
        return list_color

    list_color_creation()

    def left_click(event):
        global X,Y, colors_rgb, bandeau,click,list_color
        click = True
        X = event.x
        Y = event.y
        
        recup_coord()
        if bandeau == True and y1_final < 460 and x1_final < 440:
            
            if Y%2 == 0:
                led = (Y-1)*22+X

            else:
                led = Y*22-X

            carre = C.create_rectangle(coord, fill = colors[1], outline="")

            # Pour mettre dans une liste pour afficher avec image maker
            x = coord[0]//20
            y = (coord[1]//20)-1

            if y%2 == 0:
                led = 22*x+y

            else:
                led = 22*x+21-y

            
            list_color[y][x][0] = led
            list_color[y][x][1] = colors_rgb[0]
            list_color[y][x][2] = colors_rgb[1]
            list_color[y][x][3] = colors_rgb[2]
            print(list_color)
            

    def right_click(event):
        global X,Y,colors, bandeau, x1_final, y1_final
        X = event.x
        Y = event.y
        colors = "#000000"

        recup_coord()
        if bandeau == True and y1_final < 460 and x1_final < 440:
            carre = C.create_rectangle(coord, fill = colors, outline="")

    scribble.bind('<B1-Motion>',left_click)
    scribble.bind('<B3-Motion>',right_click)

    def recup_coord():
        global X,Y,coord, bandeau, x1_final, y1_final
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
        global img,image, x, y, h, w
        x = C.winfo_rootx()
        y = C.winfo_rooty()
        w = C.winfo_width()
        h = C.winfo_height()
        img= ImageGrab.grab((x+2, y+20, x+w-4, y+h-4)).save("images/scribble_creation/IMAGE-"+ str(len(listdir(Path(__file__).parents[1] / 'images/scribble_creation'))+1) +".jpg")
        image = True
        
    def print_image():
        global image
        if image == True:
            image_maker("scribble_creation", list_color)
            image = False

        else:
            img= ImageGrab.grab((x+2, y+20, x+w-4, y+h-4)).save("images/scribble_creation/IMAGE-"+ str(len(listdir(Path(__file__).parents[1] / 'images/scribble_creation'))+1) +".jpg")
            image_maker("scribble_creation", list_color)
            remove("images/scribble_creation/IMAGE-"+ str(len(listdir(Path(__file__).parents[1] / 'images/scribble_creation'))+1) +".jpg")

    def destroy():
        C.delete('all')
        list_color_creation()

    tk.Button(scribble, text='Exporter image_pixel', command=export_image).grid(row = 0, column=1)
    tk.Button(scribble, text='Afficher image_pixel sur les leds', command=print_image).grid(row = 0, column=2)
    tk.Button(scribble, text='Supprimer dessin', command=destroy).grid(row = 0, column=3)


    #Affichage de la fenêtre Canvas
    C.grid(row=1, column=0, columnspan=4)
    scribble.mainloop()

if __name__ == "__main__":
    scribble() 