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
		if self.movingRight == True:
			self.rect.x += self.speed
		if self.movingLeft == True:
			self.rect.x -= self.speed
		if self.movingDown == True:
			self.rect.y += self.speed
		if self.movingUp == True:
			self.rect.y -= self.speed
		
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_w:
						player_1.movingUp = True
					if event.key == pygame.K_s:
						player_1.movingDown = True
					if event.key == pygame.K_a:
						player_1.movingLeft = True
					if event.key == pygame.K_d:
						player_1.movingRight = True
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w:
						player_1.movingUp = False
					if event.key == pygame.K_s:
						player_1.movingDown = False
					if event.key == pygame.K_a:
						player_1.movingLeft = False
					if event.key == pygame.K_d:
						player_1.movingRight = False


player_1 = Player(100, 100)




