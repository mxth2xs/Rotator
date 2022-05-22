# +----- Import libs -----+ #
import time
# +-----------------------+ #

num_pixels = 22*22

# +----- Color constants -----+ #
RED=(255,0,0)
BLUE=(0,255,0)
GREEN=(0,0,255)
WHITE=(255,255,255)
CLEAR=(0,0,0)
# +---------------------------+ #


# +----- Make the snake board a grid of two dimentions -----+ #

def matrix_grid():
    matrix = []
    for i in range(num_pixels//22):
        matrix.append(["+" for j in range(22)])
    #print(matrix)
    return matrix

def printed_matrix(matrix):
    printed_matrix = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            printed_matrix += matrix[i][j] + " "
        printed_matrix += "\n"
    return printed_matrix
# +---------------------------------------------------------+ #


# +----- Animaion -----+ #
    
matrix = matrix_grid()

for i in range(len(matrix)):
    #make the first and last LED a '0' of each line
    matrix[i][-1] = "0"
    matrix[i][0] = "0"

    #make the whole first and last line '0'
    matrix[0][i] = '0'
    matrix[-1][i] = '0'

print()


#print(printed_matrix(matrix))
for line in matrix: print(line)


indices = []
for i in range(len(matrix)):
    indices += [(i,index) for index, element in enumerate(matrix[i]) if element == '0']
"""
for index, element in enumerate(matrix[i]):
    if element == '0':
        indices.append([i,index]) 
        print(indices)
"""
print(indices)
LED_list = []
for led in indices:
    LED_list.append((led[0]*22)+led[1])
print (LED_list)
#for index in indices:


