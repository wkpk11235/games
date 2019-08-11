"""Fast pygame programming

Usage:

mouse: x,y,dx,dy

quitInfo: quit_time, quit_frame

"""

mainLoop=True #required
fps=60 #required
screensize=(800,600) #required
screenc=(0,0,0) #screen color,required
title="Testing" #required

def give_pygame(module): #required
    global pygame #required
    pygame=module #required
def init(): #required
    pass

def update(screen,mouse): #required
    pass

def register_keypress(key): #required
    pass

def register_keyshift(key): #required
    pass

def onQuit(quitInfo): #required
    pass

if __name__=="__main__": #required
    import service #required
    service.init(__file__)#required
