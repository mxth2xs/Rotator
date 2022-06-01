def scribble():
    import tkinter as tk
    from tkinter.colorchooser import askcolor

    #Lancement de la fenêtre Canvas
    scribble = tk.Tk()
    C = tk.Canvas(scribble, bg="white", height=440+20, width=440)


    def change_color():
        global colors
        colors = askcolor(title="Tkinter Color Chooser")
        scribble.configure(bg=colors[1])


    tk.Button(scribble, text='Select a Color', command=change_color).pack(expand=True)

    def left_click(event):
        global X,Y, colors, bandeau
        X = event.x
        Y = event.y
        recup_coord()
        if bandeau == True:
            carre = C.create_rectangle(coord, fill = colors[1])
    
    def right_click(event):
        global X,Y,colors, bandeau 
        X = event.x
        Y = event.y
        colors = white
        recup_coord()
        if bandeau == True:
            carre = C.create_rectangle(coord, fill = colors)
        
    scribble.bind('<Button-1>',left_click)
    scribble.bind('<Button-2>',right_click)

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


    #Affichage de la fenêtre Canvas
    C.pack()
    scribble.mainloop()

    
scribble()