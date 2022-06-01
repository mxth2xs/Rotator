def SNAKEGAME(mode):
	# +------------------- Imports -------------------+ #
	import time, random
	from pynput import keyboard
	try:
		from lib.neopixel import NeoPixel
	except:
		from Algo.lib.neopixel import NeoPixel
	# +-----------------------------------------------+ #
	
	# +------------------- Options -------------------+ #
	# - Liste des options possibles
		#- Règles :
			# - Missiles : Des missiles de 2x1 traversent l'écran aléatoirement (mortels)
			# - Opposé   : snake opposé qui copie les mouvements (mortel)
			# - Blink    : food change de position après x sec
			# - Bombe	 : food devient mortelle
			# - Hidden   : food disparait après x sec
			
		#> Difficultée :
			# S++ ( x5 ):  Missiles, Opposé, Blink, Bombe, Hidden 
			# S   (x2.5):  Missiles, Opposé, Blink, Bombe 
			# A   ( x2 ):  Missiles, Opposé, Blink
			# B   (x1.5):  Missiles
			# D   ( x1 ):  X
		#> Autres :
			# N  : Lancer sans LEDs (output text)
			# M : Mario's Super Star (multicouleur et très rapide jusqu'à la 1ere nourriture mangée)
			# F : plusieurs nourritures
	
	# - Argument "mode": ex: SNAKEGAME("S++NMF")
	
	DRY = True if 'N' in mode else False
	SUPERSTAR = True if 'M' in mode else False
	MULTI = True if 'F' in mode else False
	
	if 'D' in mode: MODE = 0
	elif 'B' in mode: MODE = 1
	elif 'A' in mode: MODE = 2
	elif 'S' in mode: MODE = 3
	elif '++' in mode: MODE = 999

	
	# +-----------------------------------------------+ #

	# +----------------- Config LEDs -----------------+ #
	if not DRY: strand = NeoPixel('COM3')
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
	leds = []
	tour = 0
	# - Réinitialise les couleurs des LEDs
	if not DRY: strand.show()
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
			if not DRY:
				if playerpositions[0][0]%2 == 1: strand.setPixelColor((playerpositions[0][0]*22)+(21-playerpositions[0][1]), 0,0,0)
				else: strand.setPixelColor((playerpositions[0][0]*22)+playerpositions[0][1], 0,0,0)
				strand.show()
			playerpositions.pop(0)
		
		# En fonction de la direction, on ajoute la nouvelle coordonnée de la tete du snake.
		# - En allant vers la gauche, x est plus grand
		# - En allant vers le bas, y est plus grand
		if direction == 0: #HAUT
			# seulement la coordonnée y change : y+1
			playerpositions.append([playerpositions[-1][0]]) 
			playerpositions[-1].append(playerpositions[-2][1]+1)
		
		elif direction == 2: #BAS
			# seulement la coordonnée y change : y-1
			playerpositions.append([playerpositions[-1][0]])
			playerpositions[-1].append(playerpositions[-2][1]-1)

		elif direction == 1: #DROITE
			# seulement la coordonnée x change : x+1
			playerpositions.append([playerpositions[-1][0]+1])
			playerpositions[-1].append(playerpositions[-2][1])
		
		elif direction == 3: #GAUCHE
			# seulement la coordonnée x change : x-1
			playerpositions.append([playerpositions[-1][0]-1])
			playerpositions[-1].append(playerpositions[-2][1])
	# +-----------------------------------------------+ #

	# +------------- Fonction numéro LED -------------+ #
	def addr_LED(x,y): # inverser à cause de la disposition en zigzag des LEDs. (lignes paires et impaires)
		if   x%2 == 0: return ((x*22)+y)
		elif x%2 == 1: return ((x*22)+(21-y))
	# +-----------------------------------------------+ #

	# +-------------- Fonction drawgame --------------+ #
	def drawgame():
		"""Afficher le jeu sur les LEDs !"""
		# - Food
		if not DRY: strand.setPixelColor(addr_LED(xfood,yfood), 0,0,255)

		# - Snake
		for led in playerpositions:
			if not DRY: strand.setPixelColor(addr_LED(led[0],led[1]), 0,255,0)
			else: leds.append(addr_LED(led[0],led[1]))
		
		if not DRY:
			strand.show()
		else:	#Output text
			game_status = {
				"dir" : direction,
				"pos" : playerpositions,
				"addr" : leds,
				#"score" : score,
				#"food" : (xfood,yfood),
				#"dir_possible" : dir_possible
			}
			print(game_status)
	# +-----------------------------------------------+ #

	# +---------------- Fonction death ---------------+ #
	def death():
		"""Pour la mort du snake."""
		if not DRY:
			for led in playerpositions:
				strand.setPixelColor(addr_LED(led[0],led[1]), 0,0,0)
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
	listener = keyboard.Listener(on_press=key_press)
	listener.start()
	# +-----------------------------------------------+ #

	# +++++++++++++++++++++++++++++++++++++++++++++++++ #
	# +------------- Boucle Jeu principal ------------+ #
	# +++++++++++++++++++++++++++++++++++++++++++++++++ #

	while Game:
		# - Vitesse du jeu
		time.sleep(0.1)		

		# +------------------ Modes ------------------+ #

		#variable qui incrémente de 1 à chaque fois,
		tour += 1
		# si var >
		# +-------------------------------------------+ #


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
			if not DRY:
				strand.setPixelColor(addr_LED(xfood,yfood), 0,255,0)
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
				yfood = random.randint(0,height-1)
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
					playerpositions[-1][1]=height-1
				if playerpositions[-1][1] > height-1:
					playerpositions[-1][1]=0	
				drawgame()
		# +-----------------------------------------------+ #
	
	# +++++++++++++++++++++++++++++++++++++++++++++++++ #
	# +-----------------------------------------------+ #
	# +++++++++++++++++++++++++++++++++++++++++++++++++ #

if __name__ == "__main__":
	SNAKEGAME("dry")