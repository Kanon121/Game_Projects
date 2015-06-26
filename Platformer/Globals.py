import pygame
import os
import sys

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
MapName = "Level 1"
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
black = 0, 0, 0
playing = True

print editing
clock = pygame.time.Clock() 

def DrawWindow():

    screen.fill(black)

    
    
import Map as maps
import Entities as ent