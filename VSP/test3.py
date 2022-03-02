import pygame
import time
from pygame import image

from test2 import judge

pygame.init()

SIZE = (510, 510)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode(SIZE)
board = [[0]*3 for  i in range(3)]
turn = 1

def get_draw_pos(pos,turn):

    x,y = pos[0]//170,pos[1]//170
    if board[y][x] != 0:
        return (-1,-1)
    else:
        board[y][x]=turn
        return (x,y)
    
def judge(turn,x,y):
    if board[0][x] == board[1][x] == board[2][x]:
        return turn
    if board[y][0] == board[y][1] == board[y][2]:
        return turn
    if board[0][0] == board[1][1] == board[2][2] == turn:
        return turn
    if board[0][2] == board[1][1] == board[2][0] == turn:
        return turn
    return 0
done = False
win = False
font = pygame.font.SysFont("arialunicode",100,True,False)



o_img = pygame.image.load("o.png",(160,160))
x_img = pygame.image.load("x.png",(160,160))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            x,y = get_draw_pos(pos,turn)
            if x == -1 and y == -1:
                break
            else:
                if turn == 1:
                    screen.blit(o_img,(x*170+5,y*170+5))
                else:
                    screen.blit(x_img,(x*170+5,y*170+5))
                if judge(turn,x,y):
                    if turn == 1:
                        text = font.render("O WIN",True,BLACK)
                    else:
                        text = font.render("X WIN",True,BLACK)
                      
                    win = True
                turn *= -1

            

    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (SIZE[0]//3, 0), (SIZE[0]//3, 510))
    pygame.draw.line(screen, BLACK, (SIZE[0]//3*2, 0), (SIZE[0]//3*2, 510))
    pygame.draw.line(screen, BLACK, (0, SIZE[1]//3), (510, SIZE[1]//3))
    pygame.draw.line(screen, BLACK, (0, SIZE[1]//3*2), (510, SIZE[1]//3*2))

    pygame.display.flip()

    if win:
        
