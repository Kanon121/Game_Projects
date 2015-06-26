import Globals as gb
import pickle
# 800 / 32 = 25




class MapData():
    def __init__(self):
        self.all_tiles = []
        self.length_x = gb.width / 32
        self.length_y = gb.height / 32

        self.tiles_for_append = self.length_x * self.length_y
        self.tiles_for_x = self.length_x
        self.tiles_for_y = self.length_y      


            
          
def Save():
    with open(gb.os.getcwd() + '/saves/' + "Level 1", 'w') as f:
        pickle.dump(TileData.all_tiles, f)
        
        
def Load():
    with open(gb.os.getcwd() + '/saves/' + "Level 1", 'r') as f:
         TileData.all_tiles = pickle.load(f)
            
        
def Update():
    for tile in TileData.all_tiles:
        gb.pygame.draw.rect(gb.screen, (gb.blue), tile.rect)         



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
        TileData.all_tiles.append(self)

TileData = MapData()

def Generate_Empty():
    x = 0
    y = 0
    while  TileData.tiles_for_append != 0:
        while  TileData.tiles_for_x != 0:
            tile = Tiles(x,y)
            x += 32
            TileData.tiles_for_x -= 1
        y += 32
        x = 0
        TileData.tiles_for_y -= 1
        if TileData.tiles_for_y != 0:
            TileData.tiles_for_x = TileData.length_x
        else:
            break

