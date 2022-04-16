import tkinter as Tk

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre = Tk.Tk()
fenetre.title("Pac-man")
fenetre.config(bg=c_fond)
fenetre.geometry("320x480")

#Création du texte
txtpacfin1=Tk.Label(fenetre, text="Pac-man", fg=c_texte, bg=c_fond, font=("Cambria", 50)).grid(row=1, padx=35)
txtpacfin2=Tk.Label(fenetre, text="Score :", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=3)
txtpacfin3=Tk.Label(fenetre, text="Record :", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)

#Espacement du texte
txtepacfin1 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=2)
txtepacfin2 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=4)
txtepacfin2 = Tk.Label(fenetre, text=" ", bg=c_fond, height=2).grid(row=6)


#Création du bouton start
bouton_retry_pac = Tk.Button(fenetre, text="Réessayer", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

fenetre.mainloop()