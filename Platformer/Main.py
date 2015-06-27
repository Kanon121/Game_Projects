import Globals as gb
import Map as maps
import Entities as ent

maps.Load()
#maps.Generate_Empty()
#maps.Save()
while gb.playing == True:
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            gb.playing = False
        if e.type == gb.pygame.KEYDOWN:
            pass
    
    


	maps.Update()
	ent.player_1.Update()
	gb.clock.tick(60)   
	gb.pygame.display.flip()
	gb.DrawWindow()