import Globals as gb
import pygame



class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(10,10,10,10)
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.movingRight = False
        self.movingLeft = False
        self.movingDown = False
        self.movingUp = False
    def Update(self):
	pygame.draw.rect(gb.screen, (gb.white), player_1)

        
 
		
		
player_1 = Player(100, 100)


