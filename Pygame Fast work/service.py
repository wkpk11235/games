def init(name):
    import pygame,time,os
    module=__import__(os.path.basename(name)[:-3])
    fps=module.fps
    c=module.screenc
    pygame.display.init()
    screen=pygame.display.set_mode(module.screensize)

    pygame.display.set_caption(module.title)

    pygame.init()

    module.give_pygame(pygame)

    bgT=time.time()
    
    class quitInfo:
        def __init__(self):
            self.quitTime=time.time()-bgT
            self.quitFrame=0
        def update(self):
            self.quitTime=time.time()-bgT
            self.quitFrame+=1

    class mouse_info:
        def __init__(self):
            self.pos=pygame.mouse.get_pos()
            self.past_pos=self.pos
            self.dx=0
            self.dy=0
        def update(self):
            self.past_position=self.pos
            self.pos=pygame.mouse.get_pos()
            self.dx,self.dy=(self.pos[0]-self.past_position[0],self.pos[1]-self.past_position[1])


    pfps=fps/3*50
            

    mouse=mouse_info()
    qi=quitInfo()
    clock=pygame.time.Clock()

    module.init()
    while module.mainLoop:
        mouse.update()
        qi.update()
        screen.fill(c)
        module.update(screen,mouse)
        for event in pygame.event.get():
            if event.type==12: #quit
                pygame.quit()
                quit()
            elif event.type==2: #keydown
                module.register_keypress(event.key)
            elif event.type==3: #keyup
                module.register_keyshift(event.key)
        pygame.display.flip()
        clock.tick(pfps)
    pygame.quit()
    module.onQuit(qi)
