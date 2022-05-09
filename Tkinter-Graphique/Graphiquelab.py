import tkinter as Tk

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre = Tk.Tk()
fenetre.title("Labyrinth")
fenetre.config(bg=c_fond)
fenetre.geometry("320x480")

#Création du texte
txtlab1=Tk.Label(fenetre, text="Labyrinth", fg=c_texte, bg=c_fond, font=("Cambria", 50))
txtlab1.grid(row=1, padx=15)

txtlab2=Tk.Label(fenetre, text="Appuyez sur les boutons \n pour trouver le bon chemin \n et sortir du labyrinth", fg=c_texte, bg=c_fond, font=("Cambria",18)).grid(row=3, padx=10)

txtlab3=Tk.Label(fenetre, text="Appuyez sur \n start !!", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)

#Espacement du texte
txtelab1 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=2)
txtelab2 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=4)
txtelab3 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=6)


#Création du bouton start
bouton_start_lab = Tk.Button(fenetre, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

fenetre.mainloop()