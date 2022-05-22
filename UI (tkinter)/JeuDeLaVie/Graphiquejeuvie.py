import tkinter as Tk
#import tkinter.font as font

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre = Tk.Tk()
fenetre.title("Jeu de la vie")
fenetre.config(bg=c_fond)
fenetre.geometry("320x480")

#Création du texte
txtvie1 = Tk.Label(fenetre, text="Jeu de la vie", fg=c_texte, bg=c_fond, font=("Cambria",40))
txtvie1.grid(row=0, padx=20)

txtvie2 = Tk.Label(fenetre, text="Déplacez vous \n avec les boutons \n et créez le schéma \n de départ...", fg=c_texte, bg=c_fond, font=("Cambria", 25))
txtvie2.grid(row=2, padx=25)

txtvie3 = Tk.Label(fenetre, text="Appuyez sur \n start !!!", fg=c_texte, bg=c_fond, font=("Cambria",30))
txtvie3.grid(row=4)

#Texte d'espacement entre les widgets
txtevie1 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=1)
txtevie2 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=3)
txtevie3 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=5)

#Création du bouton start
bouton_start_vie = Tk.Button(fenetre, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=6)

#Images
#croixrouge = Tk.Label(image="croixrouge.ppm")
#croixrouge.grid(row=0, column=1)
fenetre.mainloop()