import time, random
import board, neopixel
from pynput.keyboard import Listener


#LED setup
pixel_pin = board.D18
num_pixels = 22*22
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

#'dimensions' du plan
width=22
if num_pixels == 22*22*2:height=44
else: height=22


#Snake game
def SNAKEGAME():

	def MAIN_GAME():
			
		#Initialisation
		# - Couleurs
		ROUGE=(255,0,0)
		BLEU=(0,255,0)
		VERT=(0,0,255)
		NOIR=(0,0,0)
		
		# - ...
		Game = True
		keys= [False, False, False, False]
		foodonscreen = False
		xfood, yfood = 0,0
		delete = False
		foodcords = True
		waitforanswer = True
		score = -1

		# Réinitialise les couleurs des LEDs
		pixels.fill(NOIR)

		# - positions initiales du joueur
		playerpositions = [[0,0],[1,0],[2,0]]
		#- direction initiale (droite).
		direction = 1

		# - association des direction opposées
		dir_reverse = {1:3,2:0,3:1,0:2}
		# - directions possibles en fonction de la direction du snake...
		dir_possible = [i for i in range(4) if i != direction and i != dir_reverse[direction]]
		
		
		# Fonction pour ajouter un pixel à la fin du snake lorsqu'il bouge.
		def addnewpiece(direction, delete):
			#lorsque le snake bouge, enlever le premier element de la liste des positions...
			if delete == False:
				playerpositions.pop(0)
			
			#..., en fonction de la direction, on ajoute la nouvelle coordonnée de la tete du snake.
			
			if direction == 0: #Vers le HAUT
				# seulement la coordonnée y change : y-1
				playerpositions.append([playerpositions[-1][0]]) 
				playerpositions[-1].append(playerpositions[-2][1]-1)
			
			elif direction == 2: #Vers le BAS
				# seulement la coordonnée y change : y+1
				playerpositions.append([playerpositions[-1][0]])
				playerpositions[-1].append(playerpositions[-2][1]+1)

			elif direction == 1: #Vers la DROITE
				# seulement la coordonnée x change : x+1
				playerpositions.append([playerpositions[-1][0]+1]) # x+1
				playerpositions[-1].append(playerpositions[-2][1])
			
			elif direction == 3: #Vers la GAUCHE
				# seulement la coordonnée x change : x-1
				playerpositions.append([playerpositions[-1][0]-1])
				playerpositions[-1].append(playerpositions[-2][1])
		
		#Fonction pour afficher le jeu sur les LEDs ! 
		def drawgame():
			
			#Afficher la food
			if xfood%2==1:
				pixels[(xfood*22)+(21-yfood)] = BLEU
			elif xfood%2==0:
				pixels[(xfood*22)+yfood] = BLEU

			#Afficher le snake
			for led in playerpositions:

				if led[0]%2==1:
					pixels[(led[0]*22)+(21-led[1])] = VERT	
				elif led[0]%2==0:
					pixels[(led[0]*22)+led[1]] = VERT

			pixels.show()

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
			
		#Fonction pour arreter lorsque le snake est décédé (RIP)
		def death():
			drawgame()
			print("RIP.")
			#animation
			pixels.fill(ROUGE)
			pixels.show()
			exit(0)
		
		#Actualisation des LEDs
		drawgame()

		#Tant que la partie est lancée
		while Game:
			#tempo
			time.sleep(0.1)
			#
			pixels.fill(NOIR)

			"""	
				#Check if the event is the x button
				if event.type==pygame.QUIT:
					#If it is, quit the game pygame.quit()
					pygame.quit()
					exit(0)
			"""

			#A TESTER
			#Attend qu'une touche soit pressée, puis arrête d'écouter.
			def key_press(key):
				#if the direction associated with the key is in the possible direction list, then do it, else don't.
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
					dir_possible = [i for i in range(4) if i != direction and i != dir_reverse[direction]]
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

					#print(f"food : {xfood, yfood}")
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

		#On attend une réponse pour redémarrer le jeu...
		while waitforanswer:	
			def key_press_p(key):
				if key=='p':
					print('RESTARTING')
					MAIN_GAME()
					return False #A TESTER
				
			with Listener(
					on_press=key_press_p) as listener:
				listener.join()


	MAIN_GAME()


SNAKEGAME()