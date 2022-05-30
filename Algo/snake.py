def SNAKEGAME():
	# +------------------- Imports -------------------+ #
	import time, random
	from pynput.keyboard import Listener
	import GitHub_Repos.NeoPixelUno.neopixel.neopixel as neopixel
	# +-----------------------------------------------+ #
	
	# +----------------- Config LEDs -----------------+ #
	strand = neopixel.NeoPixel('/dev/ttyACM0')
	num_pixels = 22*22
	width=22
	height = num_pixels//width
	# +-----------------------------------------------+ #
	

	def MAIN_GAME():
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
			#NeoPixel.fillPixels(strand,0,0,0)
			#strand.show()
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
				playerpositions.pop(0)
			
			# En fonction de la direction, on ajoute la nouvelle coordonnée de la tete du snake.
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
			if xfood%2 == 1: # inverser à cause de la disposition en zigzag.
				strand.setPixelColor((xfood*22)+(22-yfood), 0,255,0)
			else:
				strand.setPixelColor((xfood*22)+yfood, 0,255,0)

			# - Snake
			for led in playerpositions:
				if led[0]%2 == 1: # inverser à cause de la disposition en zigzag.
					strand.setPixelColor((led[0]*22)+(22-led[1]), 0,255,0)
				else:
					strand.setPixelColor((led[0]*22)+led[1], 0,0,255)
			
			strand.show()
			
			#Output text (optionnel)
			"""game_status = {
				#"dir" : f"{direction_text[direction]} ({direction})",
				"taille" : len(playerpositions),
				"score" : score,
				#"positions" : playerpositions,
				"food" : (xfood,yfood),
				"dir_possible" : dir_possible
				}
			print(game_status)"""
		# +-----------------------------------------------+ #

		# +---------------- Fonction death ---------------+ #
		def death():
			"""
			Pour la mort du snake.	
			"""
			drawgame()
			
			#ecran 'game over'
			f = open('./99.autres/snake_game_over.txt')
			game_over = f.read()
			f.close()
			for led in range(len(strand)):
				strand.setPixelColor(led, game_over[led][0],game_over[led][1],game_over[led][2])
			strand.show()

			#récupérer le record
			f = open('./99.autres/snake_highscore.txt', 'r')
			record = int(f.readline())
			f.close()
			#comparer le score du joueur et le record
			gagnant = 0
			if score > record:
				record = score
				gagnant = 1
			
			#Le fichier a trois lignes : 1) le record ; 2) le score du joueur ; 3) 1 ou 0 en fonction de si le joueur à battu le record.
			f = open('./99.autres/snake_highscore.txt', 'w')
			f.write(f"{record}\n{score}\n{gagnant}")
			f.close()	
		# +-----------------------------------------------+ #

		# +------------- Boucle Jeu principal ------------+ #

		#Actualisation des LEDs
		drawgame()

		#Tant que la partie est lancée
		while Game:
			# - Vitesse du jeu
			time.sleep(0.1)

			# - Attend qu'une touche soit pressée, puis arrête d'écouter.
			def key_press(key):
				"""
				:param key: (z,s,d,q) Touches pour diriger le snake.
				"""
				if key=='z' and 0 in dir_possible:
					keys[0]=True
					return False
				elif key=='d' and 1 in dir_possible:
					keys[1]=True
					return False
				elif key=='s' and 2 in dir_possible:
					keys[2]=True
					return False
				elif key=='q' and 3 in dir_possible:
					keys[3]=True
					return False
			
			with Listener(
					on_press=key_press) as listener:
				listener.join()

			#Changer la direction du snake en fonction de l'input reçu
			# - Pour chaque touche, si la touche a été pressée :
			for x in range(len(keys)):
				if keys[x] == True:
					# - changer à la direction associée,
					direction = x
					# - actualiser la liste des directions possibles.
					dir_possible = [(direction+1)%4, (direction+3)%4]
					# - déactiver la touche
					keys[x] = False
			
			#Vérifier si une food a été mangée
			if playerpositions[-1] == [xfood, yfood]:
				foodonscreen = False
				delete = True
				addnewpiece(direction, delete)
			else:
				#Changer les positions des pixels du snake
				delete = False
				addnewpiece(direction, delete)
			
			# Placer la food si elle n'est pas affiichée
			if foodonscreen == False:
				foodcords = True
				while foodcords:
					xfood = random.randint(0,width)
					yfood = random.randint(0,height)

					#Actualiser le score
					score += 1
					foodcords = False
					if [xfood, yfood] in playerpositions:
						foodcords = True
						
					foodonscreen = True
					
			# Conditions de mort du snake...
			snake_body = playerpositions[:-3]
			snake_head = playerpositions[-3:]
			for i in snake_body:
				# ...si le snake se touche lui-même
				if i in snake_head:
					Game = False
					death()
			# ...si le snake sort du plan (gauche ou droite)...
			else:
				if playerpositions[-1][0] < 0 or playerpositions[-1][0] > width :
					Game = False
					death()
				
				# ...pour le haut et le bas, le snake est juste déplacé, et on affiche les nouvelles positions
				else:
					if playerpositions[-1][1] < 0:
						playerpositions[-1][1]=height
					#print("Switch : top -> bottom")
					if playerpositions[-1][1] > height:
						playerpositions[-1][1]=0	
					#print("Switch : bottom -> top")					

					drawgame()
		# +-----------------------------------------------+ #


		

	MAIN_GAME()

SNAKEGAME()
