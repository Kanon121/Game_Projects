import Globals as gb




class player():
    def __init__(self, x, y):
        self.rect = pygame.Rect(10,10,10,10)
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.movingRight = False
        self.movingLeft = False
        self.movingDown = False
        self.movingUp = False
        
        
 
		
		
player_1 = player(100, 100)

Update(self):
	pygame.draw.rect(screen, (white), player_1)

