from tkinter import *
import tkinter.font as font

fenetre = Tk()
fenetre.title("Rotator")
fenetre.config(bg="grey")
fenetre.geometry("320x480")


#Création du texte
txt1 = Label(fenetre, text="Rotator", fg="white", bg="grey", font=("Cambria",50))
txt1.grid(row=1, column=0)
txt2 = Label(fenetre, text="Choisissez votre jeu :", fg="white", bg="grey", font=("Cambria",20))
txt2.grid(row=2)

#Texte d'espacement entre les widgets
txte2=Label(fenetre, text=" ", bg="grey")
txte2.grid(row=3)

txte4=Label(fenetre, text=" ", bg="grey")
txte4.grid(row=5)

txte5=Label(fenetre, text=" ", bg="grey")
txte5.grid(row=7)

txte6=Label(fenetre, text=" ", bg="grey")
txte6.grid(row=9)


#Création des différents boutons

bouton_vie = Button(fenetre, text="Le jeu de la vie", fg="white", bg="#999999", width=40, height=3)
bouton_vie.grid(row=4, padx=15)

bouton_lab = Button(fenetre, text="Labyrinth", fg="white", bg="#999999", width=40, height=3)
bouton_lab.grid(row=6, padx=15)

bouton_snake = Button(fenetre, text="Snake", fg="white", bg="#999999", width=40, height=3)
bouton_snake.grid(row=8, padx=15)

bouton_pacman = Button(fenetre, text="Pacman", fg="white", bg="#999999", width=40, height=3)
bouton_pacman.grid(row=10, padx=15)


fenetre.mainloop()