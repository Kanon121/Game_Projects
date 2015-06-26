import pygame
import os
import sys
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

editing = False
try: 
    arg = sys.argv[1]
    print sys.argv[1]
    if arg == "-edit":
        editing = True
        
except IndexError:
    pass

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

playing = True

print editing
clock = pygame.time.Clock() 

def DrawWindow():
    black = 0, 0, 0
    screen.fill(black)
