# -*- coding: utf-8 -*-




#import modules

import pygame

import random

import time

def generate_apple():
    appleX = random.randint(0,49) * 10
    appleY = random.randint(0,49) * 10
    return appleX, appleY
    
def draw_apple(appleX,appleY):
    pygame.draw.rect(display,apple_color,pygame.Rect(appleX,appleY,10,10))
    
def collision_with_apple(snake_head, appleX, appleY, hit, score):
    if (snake_head[0] == appleX and snake_head[1] == appleY):
        appleX, appleY = generate_apple()
        hit = True
        score += 1
    return appleX, appleY, hit, score


def collision_with_boundaries(snake_head):

    #if snake is outside of boundaries return 1
    if snake_head[0]>=display_width or snake_head[0]<0 or snake_head[1]>=display_height or snake_head[1]<0:
        return 1
    else:
        return 0
def generate_snake(snake_head, snake_position, button_direction, hit):

    #uses button_direction to decide where snake head will go
    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10
    
    snake_position.insert(0, list(snake_head))
    snake_position.pop()
    
    if hit:    
        snake_position.insert(0, list(snake_head))
        hit = False
            
    return snake_position, hit 

    
 
def display_snake(snake_position):

    #uses list of snake's positions to display snake
    for position in snake_position:
        pygame.draw.rect(display,player_color,pygame.Rect(position[0],position[1],10,10))
      

def play_game(snake_head, snake_position, button_direction):

    crashed = False
    appleX, appleY = generate_apple()
    hit = False
    score = 0
    
    while crashed is not True:

        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashed = True

            #sets variable used to move snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button_direction = 0
                elif event.key == pygame.K_RIGHT:
                    button_direction = 1
                elif event.key == pygame.K_UP:
                    button_direction = 3
                elif event.key == pygame.K_DOWN:
                    button_direction = 2                    

        #moves snake position
        snake_position, hit = generate_snake(snake_head, snake_position, button_direction, hit)
        
        appleX, appleY, hit, score = collision_with_apple(snake_head, appleX, appleY, hit, score)
        #display background and snake
        display.fill(window_color)
        display_snake(snake_position)
        draw_apple(appleX,appleY)
        pygame.display.update()
        
        #ends game loop if snake leaves the boundary
        if collision_with_boundaries(snake_head) == 1:
            
            crashed = True

        clock.tick(20)



if __name__ == "__main__":

    # set variables

    display_width = 500

    display_height = 500

    player_color = (0,191,255)

    window_color = (0,128,0)

    clock=pygame.time.Clock()
    
    apple_color = (255,0,0)

    

    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]
    

    #initialize pygame modules    

    pygame.init()

    

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")
    
    generate_apple()

    pygame.display.update()
    
    

    #start the game loop

    play_game(snake_head, snake_position, 1)



    pygame.quit()