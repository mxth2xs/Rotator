import tkinter as Tk

c_fond = "#505166"
c_bouton = "#69657f"
c_texte = "#ffffff"

fenetre = Tk.Tk()
fenetre.title("Snake")
fenetre.config(bg=c_fond)
fenetre.geometry("320x480")

#Création du texte
txtsnake1=Tk.Label(fenetre, text="Snake", fg=c_texte, bg=c_fond, font=("Cambria", 50))
txtsnake1.grid(row=1, padx=70)

txtsnake2=Tk.Label(fenetre, text="Faites grandir votre serpent, \n il ne faut pas qu'il rentre \n en collision avec lui-même \n ou un des murs", fg=c_texte, bg=c_fond, font=("Cambria",18)).grid(row=3, padx=10)

txtsnake3=Tk.Label(fenetre, text="Appuyez sur \n start !!", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)

#Espacement du texte
txtesnake1 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=2)
txtesnake2 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=4)
txtesnake2 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=6)


#Création du bouton start
bouton_start_snake = Tk.Button(fenetre, text="Start", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

fenetre.mainloop()