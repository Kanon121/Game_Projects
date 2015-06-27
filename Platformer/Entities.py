import Globals as gb
import pygame



class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(10,10,10,10)
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.color = gb.blue
        self.Onground = False
        self.jumping = False
        self.jumpHeight = 20
        self.jumpStrength = 5
        self.jumpMod = 1.6
        
        
    def Draw(self):
        
        pygame.draw.rect(gb.screen, (self.color), self.rect)



    def Gravity(self):
        for tile in gb.maps.TileData.all_tiles:         
            if tile.rect.top == self.rect.bottom:
                roundX = int(round(self.rect.x / 32))
                if tile.Xpos  == roundX:
                    if tile.is_wall:
                        self.Onground = True
                        self.jumping = False
                        self.jumpHeight = 20
                        self.jumpStrength = 4
                else:
                    self.Onground = False
        if self.Onground == False:
            self.Move("down")
            
    def Move(self, e):
        spx = self.speed
        spy = self.speed
        if e != "pass":  

            if e == "jump":
                if self.jumpHeight >= 0:
                    self.jumping = True
                    self.jumpHeight -= 1

                    dy = -(self.speed * self.jumpStrength)
                    self.jumpStrength * self.jumpMod
                    dx = 0
                else:
                    dy = 0 
                    dx = 0
                
            if e == "down":
                dx = 0
                dy = spy + 2
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




