import Globals as gb
import pygame



class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(10,10,10,10)
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.color = gb.blue

    def Draw(self):
        pygame.draw.rect(gb.screen, (self.color), self.rect)

	
    def Update(self, e):
        
        
        
        spx = self.speed
        spy = self.speed
        if e == "up":
            self.Move(0, -spy)
        if e =="down":
            self.Move(0, spy)
        if e == "left":
            self.Move(-spx, 0)
        if e == "right":
            self.Move(spx, 0)
                



                   
            
    def Move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        gb.maps.CheckCollisions(self, dx, dy)
        
        

        

            

player_1 = Player(100, 100)




