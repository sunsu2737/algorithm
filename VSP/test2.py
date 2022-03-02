import pygame
import random
pygame.init()

size = [510,510]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("test")

done = False
clock = pygame.time.Clock()
board=[['0']*3 for _ in range(3)]
turn = "O"
O_img = pygame.image.load('o.png')
X_img = pygame.image.load('x.png')

O_img = pygame.transform.scale(O_img,(160,160))
X_img = pygame.transform.scale(X_img,(160,160))
screen.fill((255,255,255))
pygame.draw.line(screen,(0,0,0),[0,170],[510,170])
pygame.draw.line(screen,(0,0,0),[0,340],[510,340])
pygame.draw.line(screen,(0,0,0),[170,0],[170,510])
pygame.draw.line(screen,(0,0,0),[340,0],[340,510])

font=pygame.font.SysFont("arialunicode",100,True,False)
def draw_OX(turn,pos):
    x, y =pos[0]//170,pos[1]//170
    if board[y][x]=='0':
        board[y][x]=turn
        f=judge(turn,x,y)
        
        if turn =='O':
            screen.blit(O_img,[x*170+5,y*170+5])
            turn = 'X'
        else:
            screen.blit(X_img,[x*170+5,y*170+5])
            turn = 'O'
        return (f,turn)
def judge(turn,x,y):
    if board[0][x]== board[1][x] == board[2][x]:
        return turn
    if board[y][0] == board[y][1] == board[y][2]:
        return turn
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '0':
        return turn
    if board[2][0] ==board[1][1] == board[0][2] and board[0][2] !='0':
        return turn
    return 'n'

while not done:

    clock.tick(10)
    for event in pygame.event.get():# User did something
        if event.type == pygame.QUIT:# If user clicked close
            done=True
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            
            f,turn=draw_OX(turn,pos)
            print(*board[0])
            print(*board[1])
            print(*board[2])
            print(f)
            if f!='n':
                screen.fill((255,255,255))
                text = font.render(f+" win!",True,(0,0,0))
                screen.blit(text,[100,180])

            

    # x,y,z = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    pygame.display.flip()