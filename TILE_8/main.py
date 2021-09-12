import pygame
import time
import random

pygame.init()

WIN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("8 TILE GAME")
icon = pygame.image.load('.\TILE_8\8.png')
pygame.display.set_icon(icon)

# FONTS
headerfont = pygame.font.Font('.\TILE_8\Subtle_Curves.ttf', 60)
header = headerfont.render("8-TILE GAME", True, (255,255,255))
numfont = pygame.font.Font('.\TILE_8\Cocogoose Pro Italic-trial.ttf', 60)
counter = pygame.font.Font('.\TILE_8\Subtle_Curves.ttf', 20)
resultfont = pygame.font.Font('.\TILE_8\Prototype.ttf', 60)
errortxt = resultfont.render('INVALID MOVE!!', True, (255, 255, 255))
wintext = resultfont.render('YOU WON!!', True, (255, 255, 255))

def printNum(num, x, y):
    if(num == 1):
        x = x + 5
    WIN.blit(numfont.render(str(num), True, (40, 44, 52)), (x+17, y))

def printCount() :
    WIN.blit(counter.render('Moves Made : '+str(numMoves), True, (255, 255, 255)), (3, 570))


# IMAGES
fillsq = pygame.image.load('.\TILE_8\\filled.png')
blanksq = pygame.image.load('.\TILE_8\\blank.png')

points = [
    [[265, 150], [365, 150], [465, 150]], 
    [[265, 250], [365, 250], [465, 250]],
    [[265, 350], [365, 350], [465, 350]]
]

mat = [
    [1,2,3],
    [4,'X',5],
    [6,7,8]
]

coor = [-1, -1]
numMoves = 0
fps = 60
clock = pygame.time.Clock()
running = True

def genConfig():
    bank = [1,2,3,4,5,6,7,'X',8]
    for i in range(3):
        for j in range(3):
            temp = random.choice(bank) 
            #temp = bank[0]
            bank.remove(temp)
            mat[i][j] = temp  
            if(mat[i][j] == 'X'):
                coor[0] = i
                coor[1] = j

def printer(mat):
    for i in range(3) :
        for j in range(3) :
            if(mat[i][j] == 'X') :
                WIN.blit(blanksq, (points[i][j][0], points[i][j][1]))
            else : 
                WIN.blit(fillsq, (points[i][j][0], points[i][j][1]))
                printNum(mat[i][j], points[i][j][0], points[i][j][1])

def def_screen():
    WIN.fill((40, 44, 52))
    WIN.blit(header, (225, 20))
    WIN.blit(headerfont.render("____________", True, (255,255,255)), (150, 30))
    printer(mat)
    printCount()

def checkConfig():
    num = 1
    if(coor[0] == 2 and coor[1] == 2):
        for i in range(3):
            for j in range(3):
                if(mat[i][j] == num):
                    num = num + 1
                else :
                    break
        if(num == 9) :
            WIN.blit(wintext, (260, 460))
            pygame.display.update()
            genConfig()
            time.sleep(3)
            
genConfig() 
while running :
    clock.tick(fps)
    def_screen()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r :
                numMoves = 0
                genConfig()
            elif event.key == pygame.K_UP:
                if(coor[0] != 0) : 
                    mat[coor[0]][coor[1]] = mat[coor[0]-1][coor[1]]
                    mat[coor[0]-1][coor[1]] = 'X'
                    coor[0] = coor[0] - 1
                    printer(mat)
                    numMoves = numMoves + 1
                else : 
                    WIN.blit(errortxt, (195, 475))
                    pygame.display.update()
                    time.sleep(3)
                checkConfig()
            elif event.key == pygame.K_DOWN :
                if(coor[0] != 2) : 
                    mat[coor[0]][coor[1]] = mat[coor[0]+1][coor[1]]
                    mat[coor[0]+1][coor[1]] = 'X'
                    coor[0] = coor[0] + 1
                    printer(mat)
                    numMoves = numMoves + 1
                else : 
                    WIN.blit(errortxt, (195, 475))
                    pygame.display.update()
                    time.sleep(3)
                checkConfig() 
            elif event.key == pygame.K_LEFT :
                if(coor[1] != 0) :  
                    mat[coor[0]][coor[1]] = mat[coor[0]][coor[1]-1]
                    mat[coor[0]][coor[1]-1] = 'X'
                    coor[1] = coor[1] - 1
                    printer(mat)
                    numMoves = numMoves + 1
                else : 
                    WIN.blit(errortxt, (195, 475))
                    pygame.display.update()
                    time.sleep(3)
                checkConfig() 
            elif event.key == pygame.K_RIGHT :
                if(coor[1] != 2) :
                    mat[coor[0]][coor[1]] = mat[coor[0]][coor[1]+1]
                    mat[coor[0]][coor[1]+1] = 'X'
                    coor[1] = coor[1] + 1
                    printer(mat)
                    numMoves = numMoves + 1
                else : 
                    WIN.blit(errortxt, (195, 475))
                    pygame.display.update()
                    time.sleep(3)
                checkConfig() 