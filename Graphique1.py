import tkinter as Tk
#import tkinter.font as font

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre = Tk.Tk()
fenetre.title("Rotator")
fenetre.config(bg=c_fond)
fenetre.geometry("320x480")


#Création du texte
txt1=Tk.Label(fenetre, text="Rotator", fg=c_texte, bg=c_fond, font=("Cambria",50))
txt1.grid(row=1, column=0)
txt2=Tk.Label(fenetre, text="Choisissez votre jeu :", fg=c_texte, bg=c_fond, font=("Cambria",20))
txt2.grid(row=2)

#Texte d'espacement entre les widgets
txte2=Tk.Label(fenetre, text=" ", bg=c_fond)
txte2.grid(row=3)

txte4=Tk.Label(fenetre, text=" ", bg=c_fond)
txte4.grid(row=5)

txte5=Tk.Label(fenetre, text=" ", bg=c_fond)
txte5.grid(row=7)

txte6=Tk.Label(fenetre, text=" ", bg=c_fond)
txte6.grid(row=9)


#Création des différents boutons

bouton_vie = Tk.Button(fenetre, text="Le jeu de la vie", fg=c_texte, bg=c_bouton, width=40, height=3)
bouton_vie.grid(row=4, padx=15)

bouton_lab = Tk.Button(fenetre, text="Labyrinth", fg=c_texte, bg=c_bouton, width=40, height=3)
bouton_lab.grid(row=6, padx=15)

bouton_snake = Tk.Button(fenetre, text="Snake", fg=c_texte, bg=c_bouton, width=40, height=3)
bouton_snake.grid(row=8, padx=15)

bouton_pacman = Tk.Button(fenetre, text="Pacman", fg=c_texte, bg=c_bouton, width=40, height=3)
bouton_pacman.grid(row=10, padx=15)


fenetre.mainloop()
