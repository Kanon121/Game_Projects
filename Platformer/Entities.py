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
		
    def Draw(self):
        pygame.draw.rect(gb.screen, (gb.blue), self.rect)
        if self.movingRight == True:
            self.rect.x += self.speed
        if self.movingLeft == True:
            self.rect.x -= self.speed
        if self.movingDown == True:
            self.rect.y += self.speed
        if self.movingUp == True:
            self.rect.y -= self.speed
            
            
    def Move(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.movingUp = True
            if event.key == pygame.K_s:
                self.movingDown = True
            if event.key == pygame.K_a:
                self.movingLeft = True
            if event.key == pygame.K_d:
                self.movingRight = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.movingUp = False
            if event.key == pygame.K_s:
                self.movingDown = False
            if event.key == pygame.K_a:
                self.movingLeft = False
            if event.key == pygame.K_d:
                self.movingRight = False


player_1 = Player(100, 100)




