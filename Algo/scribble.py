def scribble():
    import tkinter

    

    for x in range(10):
        for y in range(10):
            button = Button(Coche1,bd=10,width=7,height=3, background=couleur)
            button['command']=couleurJ(button)
            button.grid(row=y, column=x)