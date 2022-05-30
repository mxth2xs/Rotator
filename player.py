import tkinter as tk

#Import des jeux
from Algo.image_maker import image_maker
from Algo.snake import snake
#from Algo.jeudelavie import JeuDeLaVie

#import des fenetre de fin de jeu
from UI.graphiqueSnakeFin import snakeFin

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre_principale = tk.Tk()
fenetre_principale.title("Rotator")
fenetre_principale.config(bg=c_fond)
#fenetre_principale.geometry("320x480")


#Fenetre du jeu
def afficher_jeu(nom,description, padx1, padx2, jeux):
    """
    :param nom: (str) le nom du jeu, avec majuscules... ex : "Snake".
    :param description: (str) du texte, une aide, intstruction, etc...
    :param padx1: (int) padding pour le titre de la fenêtre.
    :param padx2: (int) padding pour la description de la fenêtre.
    :param jeux: (str) le nom de la fonction du jeu.
    """

    fenetre_principale.destroy()

    #fonction pour appeler le jeu en question
    def play():
        eval(jeux + "()")
        fenetre_jeu.destroy()
        
        #Pour le jeu 'snake' seulement : lorsque le jeu est terminé, appeler la fenetre de fin 
        if jeux == 'snake' :
            snakeFin()



    fenetre_jeu = tk.Tk()
    fenetre_jeu.title(nom)
    fenetre_jeu.config(bg=c_fond)
    #fenetre_jeu.geometry("320x480")

    #Création du texte
    header = tk.Label(fenetre_jeu, text=nom, fg=c_texte, bg=c_fond, font=("Cambria",40)).grid(row=0, padx=padx1)
    instructions = tk.Label(fenetre_jeu, text=description, fg=c_texte, bg=c_fond, font=("Cambria", 25)).grid(row=2, padx=padx2)
    
    #Texte d'espacement entre les widgets
    space1 = tk.Label(fenetre_jeu, text=" ", bg=c_fond).grid(row=1)
    space2 = tk.Label(fenetre_jeu, text=" ", bg=c_fond).grid(row=3)
    space3 = tk.Label(fenetre_jeu, text=" ", bg=c_fond).grid(row=5)

    #Création du bouton start
    bouton_start = tk.Button(fenetre_jeu, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15), 
        command = play
    ).grid(row=6)

    fenetre_jeu.mainloop()


#Création du texte
txt1=tk.Label(fenetre_principale, text="Rotator", fg=c_texte, bg=c_fond, font=("Cambria",50))
txt1.grid(row=1, column=0)
txt2=tk.Label(fenetre_principale, text="Choisissez votre jeu :", fg=c_texte, bg=c_fond, font=("Cambria",20))
txt2.grid(row=2)

#Texte d'espacement entre les widgets
txte2=tk.Label(fenetre_principale, text=" ", bg=c_fond)
txte2.grid(row=3)

txte4=tk.Label(fenetre_principale, text=" ", bg=c_fond)
txte4.grid(row=5)

txte5=tk.Label(fenetre_principale, text=" ", bg=c_fond)
txte5.grid(row=7)

txte6=tk.Label(fenetre_principale, text=" ", bg=c_fond)
txte6.grid(row=9)


#Création des différents boutons

bouton_vie = tk.Button(fenetre_principale, text="Le jeu de la vie", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Jeu de la vie","Déplacez vous \n avec les boutons \n et créez le schéma \n de départ...", 20, 25, "jeudelavie")
)

bouton_lab = tk.Button(fenetre_principale, text="Snake", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Snake","Faites grandir votre \n serpent, et attention \n aux murs !", 15, 10, "snake")
)

bouton_snake = tk.Button(fenetre_principale, text="Labyrinth", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Labyrinth","Trouvez le bon \n chemin et \n échappez-vous !", 45, 10, "")
)

bouton_image_maker = tk.Button(fenetre_principale, text="Image Maker", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Image Maker","Affichez l'image \n de votre choix \n en LEDs ! ", 10, 25, "image_maker") 
)

bouton_vie.grid(row=4, padx=15)
bouton_lab.grid(row=6, padx=15)
bouton_snake.grid(row=8, padx=15)
bouton_image_maker.grid(row=10, padx=15)



fenetre_principale.mainloop()
