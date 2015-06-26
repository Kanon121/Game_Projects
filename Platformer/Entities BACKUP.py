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

    def Gravity(self):
        self.Onground = False
        for tile in gb.maps.TileData.all_tiles:         
            if tile.rect.top == self.rect.bottom:
                roundX = int(round(self.rect.x / 32)
                print roundX, tile.Xpos
                if tile.Xpos  == roundX:
                    if tile.is_wall:
                        
                        self.Onground = True
                  
        if not self.Onground:
            self.rect.y += 1
    
    def Move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
        gb.maps.CheckCollisions(self, dx, dy)
        
        

        

            

player_1 = Player(100, 100)




