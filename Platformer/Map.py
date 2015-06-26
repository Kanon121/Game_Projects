import Globals as gb

# 800 / 32 = 25

all_tiles = []
length_x = gb.width / 32
length_y = gb.height / 32

tiles_for_append = length_x * length_y
tiles_for_x = length_x
tiles_for_y = length_y

if gb.width % 32 != 0:
    print "Invalid window X size"
    gb.playing = False
if gb.height % 32 != 0:
    print "Invalid window Y size"
    gb.playing = False
    

x = 0
y = 0


class Tiles():
    def __init__(self,x,y):
        self.rect = gb.pygame.Rect(32,32,32,32)
        self.rect.x = x
        self.rect.y = y
        all_tiles.append(self)


def Update():
    for tile in all_tiles:
        gb.pygame.draw.rect(gb.screen, (gb.blue), tile.rect)
        
        
while tiles_for_append != 0:
    while tiles_for_x != 0:
        tile = Tiles(x,y)
        x += 32
        tiles_for_x -= 1
    y += 32
    x = 0
    tiles_for_y -= 1
    if tiles_for_y != 0:
        tiles_for_x = length_x
    else:
        break
