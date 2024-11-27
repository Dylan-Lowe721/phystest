#Name:
#Date:
#Basic PyGame Setup Code
import math
import sys
import os.path

import pygame

import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d


pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
width, height = 500



pygame.display.set_caption("Title")


def main():
    
    pygame.init()
    window = pygame.display.set_mode((width), (height), pygame.HWSURFACE)
    
    run = True

    
    
    #physics and such
    space = pymunk.Space()
    space.gravity = Vec2d(0, -1000)
    pymunk.pygame_util.positive_y_is_up = True
    draw_options = pymunk.pygame_util.DrawOptions(window)
    
    
    
    body = pymunk.Body
   
   

while True:
    
    for event in pygame.event.get():
      # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw