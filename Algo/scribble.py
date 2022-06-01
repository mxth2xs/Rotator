def scribble():
    import tkinter as tk
    from tkinter.colorchooser import askcolor
    from pynput import mouse

    colors = [0, "#ffffff"]
    #Lancement de la fenêtre Canvas
    scribble = tk.Tk()
    C = tk.Canvas(scribble, bg="white", height=440+20, width=440)
    
    

    def change_color():
        global colors
        colors = askcolor(title="Tkinter Color Chooser")
        scribble.configure(bg=colors[1])

    tk.Button(scribble, text='Select a Color', command=change_color).pack(expand=True)

    def left_click(x,y):
        global colors, bandeau
        recup_coord(x,y)
        if bandeau == True:
            carre = C.create_rectangle(coord, fill = colors[1])
    
    def right_click(x,y):
        global colors, bandeau 
        colors = "#ffffff"
        recup_coord(x,y)
        if bandeau == True:
            carre = C.create_rectangle(coord, fill = colors)
        

    def recup_coord(x,y):
        global coord, bandeau
        if x//20 == 0 or y//20 == 0:
            if x//20 == 0 and y//20 == 0:
                x+=1
                y+=1
            elif x//20 == 0:
                x+=1
            else:
                y+=1

        if y <= 20:
            bandeau = False
        else:
            bandeau = True

        x1_final = (x//20)*20
        y1_final = (y//20)*20
        x2_final = (x//20)*20+20
        y2_final = (y//20)*20+20
        coord = x1_final, y1_final, x2_final, y2_final

    def on_click(x, y, button, pressed):
        if button == mouse.Button.left and pressed:
            left_click(x,y)
        elif button == mouse.Button.right:
            right_click(x,y)
        else:
            pass

    listener = mouse.Listener(on_click=on_click)

    listener.start()


    #Affichage de la fenêtre Canvas
    C.pack()
    scribble.mainloop()

    
scribble()