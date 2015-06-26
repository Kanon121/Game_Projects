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
    with open(gb.os.getcwd() + '/saves/' + gb.MapName, 'w') as f:
        pickle.dump(TileData.all_tiles, f)
        
        
def Load():
    with open(gb.os.getcwd() + '/saves/' + gb.MapName, 'r') as f:
         TileData.all_tiles = pickle.load(f)
            
        
def Update():
    for tile in TileData.all_tiles:
        gb.pygame.draw.rect(gb.screen, (tile.color), tile.rect)         



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
        self.color = gb.white
        self.is_wall = True
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


            
class Editor():
    def __init__(self):
        pass
    def Update(self, type):
        posx, posy = gb.pygame.mouse.get_pos()
        roundX = int(32 * round(posx / 32))
        roundY = int(32 * round(posy / 32))       
        for tile in  TileData.all_tiles:
            if type == 1:
                #left click
                 if tile.rect.collidepoint(posx, posy):
                    tile.color = gb.black
                    tile.is_wall = False
            if type == 3:
                #right click
                 if tile.rect.collidepoint(posx, posy):
                    tile.is_wall = True
                    tile.color = gb.white            
            
        
def CheckCollisions(player, dx, dy):
    for tile in TileData.all_tiles:
        if gb.ent.player_1.rect.colliderect(tile):
            if tile.is_wall:
                if dx > 0:
                    gb.ent.player_1.rect.right = tile.rect.left
                if dx < 0:
                    gb.ent.player_1.rect.left = tile.rect.right
                if dy > 0:
                    gb.ent.player_1.rect.bottom = tile.rect.top
                if dy < 0:
                    gb.ent.player_1.rect.top = tile.rect.bottom
        
        
def Edit():
    edit = Editor()
    return edit 
    
