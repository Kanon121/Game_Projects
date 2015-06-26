import pygame
import os
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

playing = True
   
clock = pygame.time.Clock() 

def DrawWindow():
    black = 0, 0, 0
    screen.fill(black)
