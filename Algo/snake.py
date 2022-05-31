def SNAKEGAME():
	# +------------------- Imports -------------------+ #
	import time, random
	from pynput import keyboard
	import lib.neopixel as neopixel
	# +-----------------------------------------------+ #
	
	# +----------------- Config LEDs -----------------+ #
	strand = neopixel.NeoPixel('COM3')
	num_led = 22*22
	width=22
	height = num_led//width
	# +-----------------------------------------------+ #

	# +----------- Initialisation générale -----------+ #
	Game = True
	keys= [False, False, False, False]
	foodonscreen = False
	xfood, yfood = 0,0
	delete = False
	foodcords = True
	score = -1

	# - Réinitialise les couleurs des LEDs
	strand.show()
	# +-----------------------------------------------+ #

	# +----------- Initialisation snake -----------+ #
	# - Positions
	playerpositions = [[0,0],[1,0],[2,0]]
	#- Direction (droite)
	direction = 1
	# - Directions possibles
	dir_possible = [(direction+1)%4, (direction+3)%4]
	# +-----------------------------------------------+ #

	# +------------- Fonction addnewpiece ------------+ #
	def addnewpiece(direction, delete):
		"""
		Ajouter un pixel à la fin de snake lorsqu'il bouge.
		:param direction: (0-3) Direction du mouvement du snake.
		:param delete: (bool) enlever ou non le 1er élément des positions.
		"""
		if delete == False:
			if playerpositions[0][1]%2 == 1: strand.setPixelColor((playerpositions[0][0]*22)+(22-playerpositions[0][1]), 0,0,0)
			else: strand.setPixelColor((playerpositions[0][0]*22)+playerpositions[0][1], 0,0,0)
			strand.show()
			playerpositions.pop(0)
		
		# En fonction de la direction, on ajoute la nouvelle coordonnée de la tete du snake.
		#!!+++ ATTENTION pour le plan : (Il est similaire au plan des canvas de tkinter.) +++!!#
		# - En allant vers la gauche, x est plus grand
		# - En allant vers le bas, y est plus grand
		if direction == 0: #HAUT
			# seulement la coordonnée y change : y-1
			playerpositions.append([playerpositions[-1][0]]) 
			playerpositions[-1].append(playerpositions[-2][1]-1)
		
		elif direction == 2: #BAS
			# seulement la coordonnée y change : y+1
			playerpositions.append([playerpositions[-1][0]])
			playerpositions[-1].append(playerpositions[-2][1]+1)

		elif direction == 1: #DROITE
			# seulement la coordonnée x change : x+1
			playerpositions.append([playerpositions[-1][0]+1]) # x+1
			playerpositions[-1].append(playerpositions[-2][1])
		
		elif direction == 3: #GAUCHE
			# seulement la coordonnée x change : x-1
			playerpositions.append([playerpositions[-1][0]-1])
			playerpositions[-1].append(playerpositions[-2][1])
	# +-----------------------------------------------+ #

	# +-------------- Fonction drawgame --------------+ #
	def drawgame():
		"""Afficher le jeu sur les LEDs !"""
		# - Food
		if yfood%2 == 1: # inverser à cause de la disposition en zigzag des LEDs.
			strand.setPixelColor((xfood*22)+(22-yfood), 0,0,255)
		else:
			strand.setPixelColor((xfood*22)+yfood, 0,0,255)

		# - Snake
		for led in playerpositions:
			if led[1]%2 == 1: # inverser...
				strand.setPixelColor((led[0]*22)+(22-led[1]), 0,255,0)
			else:
				strand.setPixelColor((led[0]*22)+led[1], 0,255,0)
		
		strand.show()
		
		#Output text (optionnel)
		"""game_status = {
			"dir" : f"{direction_text[direction]} ({direction})",
			"taille" : len(playerpositions),
			"score" : score,
			"positions" : playerpositions,
			"food" : (xfood,yfood),
			"dir_possible" : dir_possible
			}
		print(game_status)"""
	# +-----------------------------------------------+ #

	# +---------------- Fonction death ---------------+ #
	def death():
		"""Pour la mort du snake."""
		drawgame()
		
		#ecran 'game over'
		f = open('./Snake_ext/snake_game_over.txt')
		game_over = f.read()
		f.close()
		for led in range(len(num_led)):
			strand.setPixelColor(led, game_over[led][0],game_over[led][1],game_over[led][2])
		strand.show()

		#récupérer le record
		f = open('./Snake_ext/snake_highscore.txt', 'r')
		record = int(f.readline())
		f.close()
		#comparer le score du joueur et le record
		gagnant = 0
		if score > record:
			record = score
			gagnant = 1
		
		#Le fichier a trois lignes : 1) le record ; 2) le score du joueur ; 3) 1 ou 0 en fonction de si le joueur à battu le record.
		f = open('./Snake_ext/snake_highscore.txt', 'w')
		f.write(f"{record}\n{score}\n{gagnant}")
		f.close()	
	# +-----------------------------------------------+ #

	#Actualisation des LEDs
	drawgame()

	# +------- Fonction et code pour les inputs ------+ #
	def key_press(key):
		"""
		:param key: (z,s,d,q) Touches pour diriger le snake.
		"""
		if   key.char=='z' and 0 in dir_possible:  keys[0]=True
		elif key.char=='d' and 1 in dir_possible:  keys[1]=True
		elif key.char=='s' and 2 in dir_possible:  keys[2]=True
		elif key.char=='q' and 3 in dir_possible:  keys[3]=True
	
	# - Ecouter continuellement pour un input.
	listener = keyboard.Listener(
		on_press=key_press)
	listener.start()
	# +-----------------------------------------------+ #

	# +++++++++++++++++++++++++++++++++++++++++++++++++ #
	# +------------- Boucle Jeu principal ------------+ #
	# +++++++++++++++++++++++++++++++++++++++++++++++++ #

	while Game:
		# - Vitesse du jeu
		time.sleep(0.5)		

		# +----------- Changer la direction ----------+ #
		# - Pour chaque touche, si la touche a été pressée...
		for x in range(len(keys)):
			if keys[x] == True:
				# - ...changer à la direction associée,
				direction = x
				# - ...actualiser la liste des directions possibles.
				dir_possible = [(direction+1)%4, (direction+3)%4]
				# - ...désactiver la touche
				keys[x] = False
		# +-------------------------------------------+ #

		# +--------- Déplacement et nourriture -------+ #
		# - Si une food a été mangée, déplacer et rajouter un pixel
		if playerpositions[-1] == [xfood, yfood]:
			foodonscreen = False
			# - Changer la couleur de la led de nourriture
			if yfood%2 == 1: strand.setPixelColor((xfood*22)+(22-yfood), 0,255,0)
			else: strand.setPixelColor((xfood*22)+yfood, 0,255,0)
			strand.show()
			delete = True
			addnewpiece(direction, delete)
		# - Sinon, déplacer sans rajouter...
		else: 
			delete = False
			addnewpiece(direction, delete)
		# +-------------------------------------------+ #

		# +-------- Affichage de la nourriture -------+ #
		if foodonscreen == False:
			foodcords = True
			while foodcords:
				xfood = random.randint(0,width)
				yfood = random.randint(0,height)
				score += 1
				foodcords = False
				if [xfood, yfood] in playerpositions:
					foodcords = True
				foodonscreen = True
		# +-----------------------------------------------+ #

		# +---------------- Mort du snake ----------------+ #
		# - Si le snake se touche lui-même :
		snake_body = playerpositions[:-3]
		snake_head = playerpositions[-3:]
		for i in snake_body:
			if i in snake_head:
				Game = False
				death()
	
		# - Si le snake sort du plan (gauche ou droite) :
		else: # Ce 'else' est relié à la condition de nourriture à l'écran : 'if foodonscreen == False'.
			if playerpositions[-1][0] < 0 or playerpositions[-1][0] > width :
				Game = False
				death()
		# +-----------------------------------------------+ #

		# +------------ Plan infini (haut-bas) -----------+ #
			else:
				if playerpositions[-1][1] < 0:
					playerpositions[-1][1]=height
				if playerpositions[-1][1] > height:
					playerpositions[-1][1]=0	
				drawgame()
		# +-----------------------------------------------+ #
	
	# +++++++++++++++++++++++++++++++++++++++++++++++++ #
	# +-----------------------------------------------+ #
	# +++++++++++++++++++++++++++++++++++++++++++++++++ #

if __name__ == "__main__":
	SNAKEGAME()