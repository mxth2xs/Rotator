import pygame, random, time
#dfrom pygame import *
from pynput.keyboard import Listener


def MAIN_GAME():
    #pygame.init()
    
    width, height = 22, 44
    keys= [False, False, False, False]
    Game = True
    playerpositions = [[0,0],[1,0],[2,0]]
    
    direction = 1
    dir_reverse = {1:3,2:0,3:1,0:2}
    dir_possible = [i for i in range(4) if i != direction and i != dir_reverse[direction]]
    
   
    foodonscreen = False
    xfood, yfood = 0,0
    delete = False
    foodcords = True
    score = -1

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
        print("lol")
    
    def drawgame():
        
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

    drawgame()#Update the screen
    print("a")

    def key_press(key):
            """
            :param key: (z,s,d,q) Touches pour diriger le snake.
            """
            print(key)
            if key=='z' and 0 in dir_possible:
                keys[0]=True
            elif key=='d' and 1 in dir_possible:
                keys[1]=True
            elif key=='s' and 2 in dir_possible:
                keys[2]=True
            elif key=='q' and 3 in dir_possible:
                keys[3]=True
        
    
    with Listener(on_press=key_press) as listener:
        listener.start()

    while Game:
        time.sleep(1)
        
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
            
            elif playerpositions[-1][1] < 0:
                playerpositions[-1][1]=height
                print("Switch : top -> bottom")
                #deathscreen()
                #Game = False
            elif playerpositions[-1][1] > height:
                playerpositions[-1][1]=0    
                print("Switch : bottom -> top")                    
                #deathscreen()
                #Game = False
            else:
                drawgame()

            
    


MAIN_GAME()
