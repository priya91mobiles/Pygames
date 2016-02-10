import sys, pygame,random,os
import time 
from pygame.locals import *

pygame.init()
myFont = pygame.font.SysFont("monospace",15)
size = width , height = 600 , 600
black = 0 ,0, 0
speed = [1,0]

screen = pygame.display.set_mode(size)
imgPath = os.getcwd()+"/block.png" 
block = pygame.image.load(imgPath) 

bl = 9
bw = 9
headX = 207 
headY = 207

foodX = 0
foodY = 0
foodR = pygame.Rect(foodX,foodY,bl,bw)


def toString(score):
    s = ""
    l = []
    while (score != 0):
        l.append(score%10)
        score /= 10
    num = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(l)) :
        s += num[l[len(l)-i-1]]
    return s ;


score = 0
label = myFont.render("Score : 0",1,(255,255,0))

#pygame.display.flip()


rect = pygame.Rect(headX,headY,bl,bw)
snake = []
posX = []
posY = []
for i in range(6):
    snake.append(pygame.Rect(headX-i*bl,headY,bl,bw))
    posX.append(headX-i*bl)
    posY.append(headY)

pressed = 1
rt = 1
lt = -1
tp = 2
bm = -2

collision = 1 

    
def draw(snake):
    for i in range(len(snake)):
        snake[i] = pygame.Rect(posX[i],posY[i],bl,bw)
    for r in snake:
        screen.blit(block,r)
    
def update(speed):
    i = len(posX)-1
    while (i > 0):
        posX[i] = posX[i-1]
        posY[i] = posY[i-1]
        i -= 1
    posX[0] += speed[0]*bl
    posY[0] += speed[1]*bw


foodX = (random.randrange(0,600)/bl)*bl
foodY = (random.randrange(0,600)/bw)*bw    
foodR = pygame.Rect(foodX,foodY,bl,bw)
screen.blit(block,foodR)

def addBlock(pressed):
    l = len(snake)-1
    x = 0
    y = 0
    if (pressed == rt):
        x = snake[l].top
        y = snake[l].left-bw 
    if (pressed == lt):
        x = snake[l].top
        y = snake[l].right+bw
    if (pressed == tp):
        x = snake[l].bottom+bl
        y = snake[l].left
    if (pressed == bm):
        x = snake[l].bottom-bl
        y = snake[l].left
    snake.append((x,y))
    posX.append(x)
    posY.append(y)

delay = 0.1
 
while (1):
    for event in pygame.event.get() :
        if (event.type == pygame.QUIT):
            sys.exit()
        if (event.type == pygame.KEYDOWN):
            if (event.key == K_RIGHT):
                if (pressed != lt):
                    pressed = rt 
                    speed = [1,0]
            if (event.key == K_LEFT ):
                if (pressed != rt):
                    pressed = lt 
                    speed = [-1,0]
            if (event.key == K_UP ):
                if (pressed != bm):
                    pressed = tp 
                    speed = [0,-1]
            if (event.key == K_DOWN):
                if (pressed != tp):
                    pressed = bm 
                    speed = [0,1]
    
    
    screen.fill(black)
    
    
    time.sleep(delay)
    if (snake[0].colliderect(foodR)):
        score += 10
        label = myFont.render("Score : " + toString(score),1,(255,255,0))
        screen.blit(label,(500,30))
        delay = delay/1.2
        addBlock(pressed)
        foodX = (random.randrange(0,600)/bl)*bl
        foodY = (random.randrange(0,600)/bw)*bw    
        foodR = pygame.Rect(foodX,foodY,bl,bw)
    screen.blit(block,foodR)
    update(speed)
    
    draw(snake)
    screen.blit(label,(500,30))
    pygame.display.flip()
    coll = 0 
    if (snake[0].right > width+4):
        break
    if (snake[0].left < -4):
        break 
    if (snake[0].top < -4):
        break
    if (snake[0].bottom > height+4):
        break 
    
    for i in range(1,len(snake)):
        if(snake[0].colliderect(snake[i])):
            coll = 1
            break 
    if (coll == 1):
        break 
    
     
    
    
    
    
    
    