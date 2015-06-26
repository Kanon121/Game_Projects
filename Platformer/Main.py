import Globals as gb
import Map as maps


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
                if e.button == 1:
                    edit.Update()
                        
                           
    maps.Update()
    gb.clock.tick(60)   
    gb.pygame.display.flip()
    gb.DrawWindow()