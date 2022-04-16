import tkinter as Tk

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre = Tk.Tk()
fenetre.title("Jeu de la vie")
fenetre.config(bg=c_fond)
fenetre.geometry("320x480")

#Création du texte
txtviefin1=Tk.Label(fenetre, text="Jeu de la vie", fg=c_texte, bg=c_fond, font=("Cambria", 40)).grid(row=1, padx=25)
txtviefin2=Tk.Label(fenetre, text="Score :", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=3)
txtviefin3=Tk.Label(fenetre, text="Record :", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)

#Espacement du texte
txteviefin1 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=2)
txteviefin2 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=4)
txteviefin2 = Tk.Label(fenetre, text=" ", bg=c_fond, height=2).grid(row=6)


#Création du bouton start
bouton_retry_vie = Tk.Button(fenetre, text="Réessayer", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

fenetre.mainloop()