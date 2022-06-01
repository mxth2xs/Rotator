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
			###### - Opposé   : snake opposé qui copie les mouvements (mortel)
			# - Blink    : food change de position après x sec
			# - Bombe	 : va avec Blink : l'ancienne position de la food devient mortelle
			# - Hidden   : food disparait après x sec
			
		#> Difficultée :
			# S++ ( x5 ):  Missiles, #Opposé, Blink, Bombe, Hidden 
			# S   (x2.5):  Missiles, #Opposé, Blink, Bombe 
			# A   ( x2 ):  Missiles, #Opposé, Blink
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
	if '++' in mode: MODE = 999

	
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
	#Modes init
	missiles_gauche = []
	missiles_droite = []
	tempo = 0
	food_bombes = []
	MOD_tempo_hidden = 5
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

	# +------------- Fonction numéro LED -------------+ #
	def addr_LED(x,y): # inverser à cause de la disposition en zigzag des LEDs. (lignes paires et impaires)
		if   x%2 == 0: return ((x*22)+y)
		elif x%2 == 1: return ((x*22)+(21-y))
	# +-----------------------------------------------+ #

	# +------------- Fonction addnewpiece ------------+ #
	def addnewpiece(direction, delete):
		"""
		Ajouter un pixel à la fin de snake lorsqu'il bouge.
		:param direction: (0-3) Direction du mouvement du snake.
		:param delete: (bool) enlever ou non le 1er élément des positions.
		"""
		if delete == False:
			if not DRY: #Eteindre la dernière led du snake.
				strand.setPixelColor(addr_LED(playerpositions[0][0],playerpositions[0][1]), 0,0,0)
				strand.show()
			playerpositions.pop(0)
			leds.clear()
		
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

	# +-------------- Fonction drawgame --------------+ #
	def drawgame():
		"""Afficher le jeu sur les LEDs !"""
		# - Food
		if not DRY: strand.setPixelColor(addr_LED(xfood,yfood), 0,0,255)

		# - Snake
		for led in playerpositions:
			if not DRY: strand.setPixelColor(addr_LED(led[0],led[1]), 0,255,0)
			else: leds.append(addr_LED(led[0],led[1]))
		
		# - Modes
		led_missile_g = []
		led_missile_d = []
		
		if  MODE >= 1:
			for led in missiles_gauche:
				led_missile_g.append([addr_LED(led[0]-1,led[1]), addr_LED(led[0],led[1])])
				if not DRY:
					strand.setPixelColor(addr_LED(led[0],led[1]), 255,0,0)
					if led[0]-1 >= 0:
						strand.setPixelColor(addr_LED(led[0]-1,led[1]), 0,0,0)
			for led in missiles_droite:
				led_missile_d.append([addr_LED(led[0]+1,led[1]), addr_LED(led[0],led[1])])
				if not DRY:
					strand.setPixelColor(addr_LED(led[0],led[1]), 255,0,0)
					if led[0]-1 < 484:
						strand.setPixelColor(addr_LED(led[0]+1,led[1]), 0,0,0)


		if not DRY:
			strand.show()
		else:	#Output text
			game_status = {
				#"tour" : tour,
				#"tempo" : tempo,
				#"dir" : direction,
				#"pos" : playerpositions,
				#"addr" : leds,
				#"score" : score,
				#"food" : (xfood,yfood),
				#"bombes" : food_bombes,
				#"dir_possible" : dir_possible,
				#"missiles" : missiles_gauche+missiles_droite,
				"miss_L_G" : led_missile_g,
				"miss_L_D" : led_missile_d,
			}
			print(game_status)
	# +-----------------------------------------------+ #

	# +---------------- Fonction death ---------------+ #
	def death(message):
		"""Pour la mort du snake."""
		if not DRY:
			for led in playerpositions:
				strand.setPixelColor(addr_LED(led[0],led[1]), 0,0,0)
			strand.show()
		else:
			print(f"Rip. {message}")
	
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
		""":param key: (z,s,d,q) Touches pour diriger le snake."""
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

		#Temporisation pour les missiles
		if tempo > 0:
			tempo -= 1

		if MOD_tempo_hidden > 0:
			MOD_tempo_hidden -= 1

		# Blink : déplacer la nourriture tout les 20 tours.
		if MODE >= 2 and tour%20 == 0:
			foodonscreen = False
			if not DRY:strand.setPixelColor(addr_LED(xfood,yfood), 0,0,0)
			if MODE >= 3: # Bombes : l'ancienne position de la food devient mortelle
				food_bombes.append([xfood,yfood])
				if not DRY:strand.setPixelColor(addr_LED(xfood,yfood), 255,0,0) 

		# Hidden : faire disparaitre la nourriture 5 tours après son apparition.
		if MODE > 3 and MOD_tempo_hidden == 0: 
			for i in ([[xfood,yfood]]+food_bombes):
				if not DRY:strand.setPixelColor(addr_LED(i[0],i[1]), 0,0,0)

		# - Déplacer les missiles
		if tour >= 1:
			for i in missiles_gauche: 
				#if not DRY: strand.setPixelColor(addr_LED(i[0],i[1]), 0,0,0)
				if i[0] >= 21: missiles_gauche.remove(i)
				else: i[0] += 1
			for i in missiles_droite: 
				#if not DRY: strand.setPixelColor(addr_LED(i[0],i[1]), 0,0,0)
				if i[0] <= 0: missiles_droite.remove(i)
				else: i[0] -= 1

		if MODE >=1: 
			# +----- MISSILES -----+ #
			if tempo==0 and random.randint(1,5) == 1: # 20% de chance de missile
				tempo = 5
				for i in range(random.randint(1,3)): 
					missiles_gauche.append([0,random.randint(1,height-1)])	# position random
					missiles_droite.append([21,random.randint(1,height-1)])
			# +--------------------+ #

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
				MOD_tempo_hidden = 5
				foodcords = False
				if [xfood, yfood] in playerpositions:
					foodcords = True
					score += 1
				foodonscreen = True
		# +-----------------------------------------------+ #

		# +---------------- Mort du snake ----------------+ #
		# - Si le snake se touche lui-même :
		snake_body = playerpositions[:-3]
		snake_head = playerpositions[-3:]
		for i in snake_body:
			if i in snake_head:
				Game = False
				death("You ate snake...")

		# Conditions de mort MODES
		explosives = missiles_gauche + missiles_droite + food_bombes
		for i in explosives:
			if i in playerpositions:
				Game = False
				if not DRY:
					for i in explosives:
						strand.setPixelColor(addr_LED(i[0],i[1]), 255,0,0)
					strand.show()
				death("Boom.")
		# - Si le snake sort du plan (gauche ou droite) :
		else: # Ce 'else' est relié à la condition de nourriture à l'écran : 'if foodonscreen == False'.
			if playerpositions[-1][0] < 0 or playerpositions[-1][0] > width :
				Game = False
				death("You can't leave.")
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
	SNAKEGAME("S++")