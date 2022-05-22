
import pygame, random
from pygame import *

def SNAKEGAME():

	def MAIN_GAME():
		pygame.init()
		
		zoom = 20
		width, height = 22, 44
		boxSize = zoom
		screenwidth, screenheight = (width+1)*zoom, (height+1)*zoom
		screen=pygame.display.set_mode((screenwidth,screenheight))
		keys= [False, False, False, False]
		Game = True
		playerpositions = [[0,0],[1,0],[2,0]]
		
		direction = 1
		direction_text = {1:"droite", 2:"bas   ", 3:"gauche", 0:"haut  "}
		dir_reverse = {1:3,2:0,3:1,0:2}
		dir_possible = [i for i in range(4) if i != direction and i != dir_reverse[direction]]
		
		colorBlack = (0,0,0)
		colorRed = (255, 0, 0)
		colorBlue = (0,0,255)
		colorGreen = (0,255,0)
		
		foodonscreen = False
		xfood, yfood = 0,0
		delete = False
		foodcords = True
		score = -1
		waitforanswer = True

		def addnewpiece(direction, delete):#Function to add new piece to end of tail. If the snake has eaten food, dont delete the other piece.
			if delete == False:
				playerpositions.pop(0)
			if direction == 0: #Vers le HAUT
				#X value
				playerpositions.append([playerpositions[-1][0]])
				#Y value
				playerpositions[-1].append(playerpositions[-2][1]-1)
			elif direction == 1: #Vers la DROITE
				#X value of new coord
				playerpositions.append([playerpositions[-1][0]+1])#subtract one from length to call lists
				#Y value of new coord
				playerpositions[-1].append(playerpositions[-2][1])#subtract two, one for length and one to go to previous list after appended new value in previous step
			elif direction == 2: #Vers le BAS
				#X value
				playerpositions.append([playerpositions[-1][0]])
				#Y value
				playerpositions[-1].append(playerpositions[-2][1]+1)
			elif direction == 3: #Vers la GAUCHE
				#X value
				playerpositions.append([playerpositions[-1][0]-1])
				#Y value
				playerpositions[-1].append(playerpositions[-2][1])
			
		def death():#Function to draw the words for the death screen
			pygame.font.init()
			font = pygame.font.Font(None, 50)
			deathtext = font.render("You Died!", True, colorRed)
			textRect_deathtext = deathtext.get_rect()
			textRect_deathtext.centerx = screen.get_rect().centerx
			textRect_deathtext.centery = screen.get_rect().centery-60
			screen.blit(deathtext, textRect_deathtext)
			font2 = pygame.font.Font(None, 30)
			playagain = font.render("Press p to play again", True, colorRed)
			textRect_playagain = playagain.get_rect()
			textRect_playagain.centerx = screen.get_rect().centerx
			textRect_playagain.centery = screen.get_rect().centery
			screen.blit(playagain, textRect_playagain)
		
		def drawgame():
			#Draw food
			pygame.draw.rect(screen, colorBlue, (xfood*boxSize,yfood*boxSize,boxSize,boxSize), 0)
				
			#Draw snake boxes
			for i in playerpositions:
				pygame.draw.rect(screen, colorGreen, (i[0]*boxSize,i[1]*boxSize,boxSize,boxSize), 0)
			pygame.display.update()

			#Text output
			#if its not the first output (-1 for score is only for the 1st)
			game_status = {
				#"dir" : f"{direction_text[direction]} ({direction})",
				"taille" : len(playerpositions),
				"score" : score,
				#"positions" : playerpositions,
				"food" : (xfood,yfood),
				"dir_possible" : dir_possible
				}
			print(game_status)
			
			

		def deathscreen():#Function that puts all of the functions together for the death screen
			drawgame()
			death()
			pygame.display.update()
		
		drawgame()#Update the screen

		while Game:
			pygame.time.delay(100)
			screen.fill(colorBlack)
			for event in pygame.event.get():
				#Check if the event is the x button
				if event.type==pygame.QUIT:
					#If it is, quit the game pygame.quit()
					pygame.quit()
					exit(0)
				if event.type == pygame.KEYDOWN:
					#if the direction associated with the key is in the possible direction list, then do it, else don't.
					if event.key==K_z and 0 in dir_possible:
						keys[0]=True
					elif event.key==K_d and 1 in dir_possible:
						keys[1]=True
					elif event.key==K_s and 2 in dir_possible:
						keys[2]=True
					elif event.key==K_q and 3 in dir_possible:
						keys[3]=True
			#Set direction of snake
			for x in range(len(keys)):
				if keys[x] == True:
					direction = x
					dir_possible = [i for i in range(4) if i != direction and i != dir_reverse[direction]]
					keys[x] = False
					
			#Check if eaten food
			if playerpositions[-1] == [xfood, yfood]:
				foodonscreen = False
				delete = True
				addnewpiece(direction, delete)
			else:
				#Create next piece for snake
				delete = False
				addnewpiece(direction, delete)
			#Food
			if foodonscreen == False:
				foodcords = True
				while foodcords:
					xfood = random.randint(0,width)
					yfood = random.randint(0,height)

					print(f"food : {xfood, yfood}")
					score+=1
					foodcords = False
					if [xfood, yfood] in playerpositions:
						foodcords = True
						
					foodonscreen = True
					
			#Check if death
			snake_body = playerpositions[:-3]
			snake_head = playerpositions[-3:]
			for i in snake_body:
				if i in snake_head:
					print(f"{i} double.")
					deathscreen()
					Game = False
			else:#Check if snake head is out of bounds
				if playerpositions[-1][0] < 0:
					deathscreen()#If it is, end the game
					Game = False
				elif playerpositions[-1][0] > width:
					deathscreen()
					Game = False
				
				else:
					if playerpositions[-1][1] < 0:
						playerpositions[-1][1]=height
					print("Switch : top -> bottom")
					if playerpositions[-1][1] > height:
						playerpositions[-1][1]=0	
					print("Switch : bottom -> top")					

					drawgame()

				
		while waitforanswer:#This is used so the game doesnt quit immediately as it has something to wait for	
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key==K_p:
						print('RESTARTING')
						MAIN_GAME()


	MAIN_GAME()

SNAKEGAME()