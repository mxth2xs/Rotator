# +------------------- Imports -------------------+ #
import tkinter as tk
from rotator.algo.image_maker import image_maker
from rotator.algo.snake import SNAKEGAME
from rotator.algo.jeudelavie import jeudelavie
from rotator.algo.test_led import test_led
from rotator.algo.scribble import scribble
from rotator.UI.graphiqueSnakeFin import snakeFin

# +-----------------------------------------------+ #

# +------------------ Couleurs -------------------+ #
c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"
# +-----------------------------------------------+ #

# +---------- Fonction : fen des jeux ----------+ #
def afficher_jeu(nom,description, padx1, padx2, jeux):
    """
    :param nom: (str) le nom du jeu, avec majuscules... ex : "Snake".
    :param description: (str) du texte, une aide, intstruction, etc...
    :param padx1: (int) padding pour le titre de la fenêtre.
    :param padx2: (int) padding pour la description de la fenêtre.
    :param jeux: (str) le nom de la fonction du jeu.
    """

    #fonction pour appeler le jeu en question
    def play():
        eval(jeux + "()")
        fenetre_jeu.destroy()
        #Pour le jeu 'snake' seulement : lorsque le jeu est terminé, appeler la fenetre de fin 
        if jeux == 'snake' : snakeFin()

    fenetre_principale.destroy()

    fenetre_jeu = tk.Tk()
    fenetre_jeu.title(nom)
    fenetre_jeu.config(bg=c_fond)

    #Création du texte
    header =        tk.Label(fenetre_jeu, text=nom, fg=c_texte, bg=c_fond, font=("Cambria",40)).grid(row=0, padx=padx1)
    space1 =        tk.Label(fenetre_jeu, text=" ", bg=c_fond).grid(row=1)
    instructions =  tk.Label(fenetre_jeu, text=description, fg=c_texte, bg=c_fond, font=("Cambria", 25)).grid(row=2, padx=padx2)
    space2 =        tk.Label(fenetre_jeu, text=" ", bg=c_fond).grid(row=3)
    bouton_start =  tk.Button(fenetre_jeu, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15), command = play).grid(row=4)
    space3 =        tk.Label(fenetre_jeu, text=" ", bg=c_fond).grid(row=5)
    
    fenetre_jeu.mainloop()
# +-----------------------------------------------+ #

# +---------- Config fenêtre principale ----------+ #
fenetre_principale = tk.Tk()
fenetre_principale.title("Rotator")
fenetre_principale.config(bg=c_fond)
# +-----------------------------------------------+ #

# +---------- Labels fenêtre principale ----------+ #
headerrr = tk.Label(fenetre_principale, bg=c_fond, text="Rotator", fg=c_texte, font=("Cambria",50)).grid(row=1)
instruct = tk.Label(fenetre_principale, bg=c_fond, text="Choisissez votre jeu :", fg=c_texte, font=("Cambria",20)).grid(row=2)
space_r3 = tk.Label(fenetre_principale, bg=c_fond, text=" ").grid(row=3)
space_r5 = tk.Label(fenetre_principale, bg=c_fond, text=" ").grid(row=5)
space_r7 = tk.Label(fenetre_principale, bg=c_fond, text=" ").grid(row=7)
space_r9 = tk.Label(fenetre_principale, bg=c_fond, text=" ").grid(row=9)
space_r9 = tk.Label(fenetre_principale, bg=c_fond, text=" ").grid(row=11)
space_r9 = tk.Label(fenetre_principale, bg=c_fond, text=" ").grid(row=13)
space_r9 = tk.Label(fenetre_principale, bg=c_fond, text=" ").grid(row=15)
# +-----------------------------------------------+ #

# +---------- Boutons fenêtre principale ---------+ #
btn_jeudelavie = tk.Button(fenetre_principale, text="Le jeu de la vie", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Jeu de la vie","Déplacez vous \n avec les boutons \n et créez le schéma \n de départ...", 20, 25, "jeudelavie")
).grid(row=4, padx=15)

btn_snake = tk.Button(fenetre_principale, text="Snake", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Snake","Faites grandir votre \n serpent, et attention \n aux murs !", 15, 10, "SNAKEGAME")
).grid(row=6, padx=15)

btn_labyrinth = tk.Button(fenetre_principale, text="Labyrinth", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Labyrinth","Trouvez le bon \n chemin et \n échappez-vous !", 45, 10, "")
).grid(row=8, padx=15)

btn_image_maker = tk.Button(fenetre_principale, text="Image Maker", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Image Maker","Affichez l'image \n de votre choix \n en LEDs ! ", 10, 25, "image_maker") 
).grid(row=10, padx=15)

btn_image_maker = tk.Button(fenetre_principale, text="Scribble", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Test led","Juste pour tester les leds", 10, 25, "scribble") 
).grid(row=12, padx=15)

btn_image_maker = tk.Button(fenetre_principale, text="Test led", fg=c_texte, bg=c_bouton, width=40, height=3, 
    command= lambda: afficher_jeu("Test led","Juste pour tester les leds", 10, 25, "test_led") 
).grid(row=14, padx=15)
# +-----------------------------------------------+ #


fenetre_principale.mainloop()