import Globals as gb
import Map as maps
import Entities as ent

if gb.editing:
    edit = maps.Edit()


#maps.Load()
maps.Generate_Empty()
maps.Save()
while gb.playing == True:

    
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            gb.playing = False

        if e.type == gb.pygame.KEYDOWN:
            pass

        if e.type == gb.pygame.MOUSEBUTTONDOWN:
            if gb.editing:
                edit.Update(e.button)
                        
    ent.player_1.Update()                      
    maps.Update()
    gb.clock.tick(60)   
    gb.pygame.display.flip()
    gb.DrawWindow()

