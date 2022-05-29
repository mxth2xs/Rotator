def snakeFin():
    import tkinter as Tk

    c_fond = "#505166"
    c_bouton = "#69657f"
    c_texte = "#ffffff"

    fenetre = Tk.Tk()
    fenetre.title("Snake")
    fenetre.config(bg=c_fond)
    fenetre.geometry("320x480")

    #Récupérer les scores
    f = open('./99.autres/snake_highscore.txt', 'r+')
    record = int(f.readline())
    score = int(f.readline())
    gagnant = int(f.readline())
    f.close()

    #Création du texte
    if gagnant == 1:
        titre = " Bravo ! "
        padx1 = 65
    else: 
        titre = "Game Over"
        padx1 = 35

    header=Tk.Label(fenetre, text=titre, fg=c_texte, bg=c_fond, font=("Cambria", 40)).grid(row=1, padx=padx1)
    label_1=Tk.Label(fenetre, text=f"Score : {score}", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=3)
    label_2=Tk.Label(fenetre, text=f"Record : {record}", fg=c_texte, bg=c_fond, font=("Cambria", 30)).grid(row=5)


    #Espacement du texte
    txtesnake1 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=2)
    txtesnake2 = Tk.Label(fenetre, text=" ", bg=c_fond).grid(row=4)
    txtesnake3 = Tk.Label(fenetre, text=" ", bg=c_fond, height=2).grid(row=6)


    #Création du bouton start
    bouton_retry_snake = Tk.Button(fenetre, text="Réessayer", fg=c_texte, bg=c_bouton, width=25, height=2, font=("Cambria", 15)).grid(row=7)

    fenetre.mainloop()