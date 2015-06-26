import Globals as gb


if gb.editing:
    edit = gb.maps.Edit()


gb.maps.Load()
#gb.maps.Generate_Empty()
#gb.maps.Save()

while gb.playing == True:

    
    for e in gb.pygame.event.get():
        if e.type == gb.pygame.QUIT:
            gb.playing = False

        
        if e.type == gb.pygame.MOUSEBUTTONDOWN:
            if gb.editing:
                edit.Update(e.button)        
        

        
 
        key = gb.pygame.key.get_pressed()

    if key[gb.pygame.K_p]:
        gb.maps.Save()

        print gb.ent.player_1.Onground
    if key[gb.pygame.K_w]:
        gb.ent.player_1.Move("up")
    if key[gb.pygame.K_s]:
        gb.ent.player_1.Move("down")
    if key[gb.pygame.K_a]:
        gb.ent.player_1.Move("left")
    if key[gb.pygame.K_d]:
        gb.ent.player_1.Move("right")
                        
    else:
        gb.ent.player_1.Move("pass")
    gb.maps.Update()
    gb.ent.player_1.Draw()
    gb.ent.player_1.Gravity()
    gb.clock.tick(60)   
    gb.pygame.display.flip()
    gb.DrawWindow()

