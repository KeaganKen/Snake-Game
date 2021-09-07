#Importing PyGame
import pygame
from pygame.constants import KEYDOWN
import time
import random
pygame.init()

#Declaring variable to see if the game is indeed over
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
dis_width = 800
dis_height = 600
snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_height/2, dis_width/2])

#Initaliasing and setting the display up
pygame.init()
dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game by Twisterzz')



def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width/2 
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0
    foodx = round(random.randrange(0, dis_width - snake_block / 10.0) * 10.0)
    foody = round(random.randrange(0, dis_width - snake_block / 10.0) * 10.0)


    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
        
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
        
        x1 += x1_change
        y1 += y1_change

        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, 10, 10])
        pygame.display.update()
        
        

        if x1 == foodx and y1 == foody:
            print("Yummy")
        clock.tick(snake_speed)
    message("You lost", red)
    pygame.display.update()
    time.sleep(2)

    #Quits game when finished
    pygame.quit()
    quit()
gameLoop()