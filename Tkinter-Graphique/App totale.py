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

def afficher_snake():
    fenetre.destroy()
    
    fen_afficher_snake = tk.Tk()
    fen_afficher_snake.title("Snake")
    fen_afficher_snake.config(bg=c_fond)
    fen_afficher_snake.geometry("320x480")
    
    #Création du texte
    txtsnake1=tk.Label(fen_afficher_snake, text="Snake", fg=c_texte, bg=c_fond, font=("Cambria", 50))
    txtsnake1.grid(row=1, padx=70)

    txtsnake2=tk.Label(fen_afficher_snake, text="Faites grandir votre serpent, \n il ne faut pas qu'il rentre \n en collision avec lui-même \n ou un des murs", fg=c_texte, bg=c_fond, font=("Cambria",18)).grid(row=3, padx=10)

    txtsnake3=tk.Label(fen_afficher_snake, text="Appuyez sur \n start !!", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)

    #Espacement du texte
    txtesnake1 = tk.Label(fen_afficher_snake, text=" ", bg=c_fond).grid(row=2)
    txtesnake2 = tk.Label(fen_afficher_snake, text=" ", bg=c_fond).grid(row=4)
    txtesnake2 = tk.Label(fen_afficher_snake, text=" ", bg=c_fond).grid(row=6)


    #Création du bouton start
    bouton_start_snake = tk.Button(fen_afficher_snake, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

    fen_afficher_snake.mainloop()
    
def afficher_lab():
    fenetre.destroy()
    
    fen_afficher_lab = tk.Tk()
    fen_afficher_lab.title("Labyrinth")
    fen_afficher_lab.config(bg=c_fond)
    fen_afficher_lab.geometry("320x480")

    #Création du texte
    txtlab1=tk.Label(fen_afficher_lab, text="Labyrinth", fg=c_texte, bg=c_fond, font=("Cambria", 50))
    txtlab1.grid(row=1, padx=15)

    txtlab2=tk.Label(fen_afficher_lab, text="Appuyez sur les boutons \n pour trouver le bon chemin \n et sortir du labyrinth", fg=c_texte, bg=c_fond, font=("Cambria",18)).grid(row=3, padx=10)

    txtlab3=tk.Label(fen_afficher_lab, text="Appuyez sur \n start !!", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)

    #Espacement du texte
    txtelab1 = tk.Label(fen_afficher_lab, text=" ", bg=c_fond).grid(row=2)
    txtelab2 = tk.Label(fen_afficher_lab, text=" ", bg=c_fond).grid(row=4)
    txtelab3 = tk.Label(fen_afficher_lab, text=" ", bg=c_fond).grid(row=6)


    #Création du bouton start
    bouton_start_lab = tk.Button(fen_afficher_lab, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

    fen_afficher_lab.mainloop()

def afficher_pac():
  fenetre.destroy()
  
  fen_afficher_pac = tk.Tk()
  fen_afficher_pac.title("Pac-man")
  fen_afficher_pac.config(bg=c_fond)
  fen_afficher_pac.geometry("320x480")
  
  #Création du texte
  txtpac1=tk.Label(fen_afficher_pac, text="Pac-man", fg=c_texte, bg=c_fond, font=("Cambria", 50)).grid(row=1, padx=35)

  txtpac2=tk.Label(fen_afficher_pac, text="Nourrissez pac-man et \n évitez les fantômes", fg=c_texte, bg=c_fond, font=("Cambria",18)).grid(row=3, padx=10)

  txtpac3=tk.Label(fen_afficher_pac, text="Appuyez sur \n start !!", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)

  #Espacement du texte
  txtepac1 = tk.Label(fen_afficher_pac, text=" ", bg=c_fond).grid(row=2)
  txtepac2 = tk.Label(fen_afficher_pac, text=" ", bg=c_fond).grid(row=4)
  txtepac3 = tk.Label(fen_afficher_pac, text=" ", bg=c_fond).grid(row=6)


  #Création du bouton start
  bouton_start_pac = tk.Button(fen_afficher_pac, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

  fen_afficher_pac.mainloop()


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

bouton_lab = tk.Button(fenetre, text="Labyrinth", fg=c_texte, bg=c_bouton, width=40, height=3, command=afficher_lab)
bouton_lab.grid(row=6, padx=15)

bouton_snake = tk.Button(fenetre, text="Snake", fg=c_texte, bg=c_bouton, width=40, height=3, command=afficher_snake)
bouton_snake.grid(row=8, padx=15)

bouton_pacman = tk.Button(fenetre, text="Pacman", fg=c_texte, bg=c_bouton, width=40, height=3, command=afficher_pac)
bouton_pacman.grid(row=10, padx=15)


fenetre.mainloop()
