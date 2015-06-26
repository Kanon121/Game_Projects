import Globals as gb
import pygame



class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(10,10,10,10)
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.color = gb.blue
        self.Onground = False
    def Draw(self):
        
        pygame.draw.rect(gb.screen, (self.color), self.rect)



    def Gravity(self):
        for tile in gb.maps.TileData.all_tiles:         
            if tile.rect.top == self.rect.bottom:
                roundX = int(round(self.rect.x / 32))
                if tile.Xpos  == roundX:
                    if tile.is_wall:
                        self.Onground = True

                else:
                    self.Onground = False
        if self.Onground == False:
            self.Move("down")
            
    def Move(self, e):
        spx = self.speed
        spy = self.speed
        if e != "pass":  
            if e == "up":
                dx = 0
                dy = -spy
            if e =="down":
                dx = 0
                dy = spy
            if e == "left":
                dx= -spx
                dy = 0
            if e == "right":
                dx = spx
                dy = 0
            
            
            self.rect.x += dx
            self.rect.y += dy
            gb.maps.CheckCollisions(self, dx, dy)
        
        

        

            

player_1 = Player(100, 100)




