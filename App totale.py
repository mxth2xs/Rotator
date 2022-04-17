import tkinter as tk
#import tkinter.font as font

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre = tk.Tk()
fenetre.title("Rotator")
fenetre.config(bg=c_fond)
fenetre.geometry("320x480")

def afficher_vie():
    fenetre.destroy()

    fen_afficher_vie = tk.Tk()
    fen_afficher_vie.title("Jeu de la vie")
    fen_afficher_vie.config(bg=c_fond)
    fen_afficher_vie.geometry("320x480")

    #Création du texte
    txtvie1 = tk.Label(fen_afficher_vie, text="Jeu de la vie", fg=c_texte, bg=c_fond, font=("Cambria",40))
    txtvie1.grid(row=0, padx=20)

    txtvie2 = tk.Label(fen_afficher_vie, text="Déplacez vous \n avec les boutons \n et créez le schéma \n de départ...", fg=c_texte, bg=c_fond, font=("Cambria", 25))
    txtvie2.grid(row=2, padx=25)

    txtvie3 = tk.Label(fen_afficher_vie, text="Appuyez sur \n start !!!", fg=c_texte, bg=c_fond, font=("Cambria",30))
    txtvie3.grid(row=4)

    #Texte d'espacement entre les widgets
    txtevie1 = tk.Label(fen_afficher_vie, text=" ", bg=c_fond).grid(row=1)
    txtevie2 = tk.Label(fen_afficher_vie, text=" ", bg=c_fond).grid(row=3)
    txtevie3 = tk.Label(fen_afficher_vie, text=" ", bg=c_fond).grid(row=5)

    #Création du bouton start
    bouton_start_vie = tk.Button(fen_afficher_vie, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=6)

    #Images
    #croixrouge = Tk.Label(image="croixrouge.ppm")
    #croixrouge.grid(row=0, column=1)
    fen_afficher_vie.mainloop()



#Création du texte
txt1=tk.Label(fenetre, text="Rotator", fg=c_texte, bg=c_fond, font=("Cambria",50))
txt1.grid(row=1, column=0)
txt2=tk.Label(fenetre, text="Choisissez votre jeu :", fg=c_texte, bg=c_fond, font=("Cambria",20))
txt2.grid(row=2)

#Texte d'espacement entre les widgets
txte2=tk.Label(fenetre, text=" ", bg=c_fond)
txte2.grid(row=3)

txte4=tk.Label(fenetre, text=" ", bg=c_fond)
txte4.grid(row=5)

txte5=tk.Label(fenetre, text=" ", bg=c_fond)
txte5.grid(row=7)

txte6=tk.Label(fenetre, text=" ", bg=c_fond)
txte6.grid(row=9)


#Création des différents boutons

bouton_vie = tk.Button(fenetre, text="Le jeu de la vie", fg=c_texte, bg=c_bouton, width=40, height=3, command=afficher_vie)
bouton_vie.grid(row=4, padx=15)

bouton_lab = tk.Button(fenetre, text="Labyrinth", fg=c_texte, bg=c_bouton, width=40, height=3)
bouton_lab.grid(row=6, padx=15)

bouton_snake = tk.Button(fenetre, text="Snake", fg=c_texte, bg=c_bouton, width=40, height=3)
bouton_snake.grid(row=8, padx=15)

bouton_pacman = tk.Button(fenetre, text="Pacman", fg=c_texte, bg=c_bouton, width=40, height=3)
bouton_pacman.grid(row=10, padx=15)


fenetre.mainloop()
