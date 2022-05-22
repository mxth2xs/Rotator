import tkinter as Tk

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre = Tk.Tk()
fenetre.title("Pac-man")
fenetre.config(bg=c_fond)
fenetre.geometry("320x480")

#Création du texte
txtpac1=Tk.Label(fenetre, text="Pac-man", fg=c_texte, bg=c_fond, font=("Cambria", 50)).grid(row=1, padx=35)

txtpac2=Tk.Label(fenetre, text="Nourrissez pac-man et \n évitez les fantômes", fg=c_texte, bg=c_fond, font=("Cambria",18)).grid(row=3, padx=10)

txtpac3=Tk.Label(fenetre, text="Appuyez sur \n start !!", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)

#Espacement du texte
txtepac1 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=2)
txtepac2 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=4)
txtepac3 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=6)


#Création du bouton start
bouton_start_pac = Tk.Button(fenetre, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

fenetre.mainloop()