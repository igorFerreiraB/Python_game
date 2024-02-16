import pygame
from sys import exit

width = 1280   #variable for screen width
height = 720   #variable for screen height
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')


while True:
    screen.fill((0,0,0))  #fill the screen background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    #check for closing game window
            pygame.quit()
            exit()
    pygame.display.update()   #update screen
    clock.tick(60)

    pygame.draw.circle(screen, (0, 250, 0), (width/2, height/2), 50)

