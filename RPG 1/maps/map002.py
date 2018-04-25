from scripts import objects

def Init():
    global players,portals,bricks
    objects.allobjs=[]

    #temp boi
    global player
    player=objects.Player("sans.png",0,0)
    #boi boi

def Update(events):
    player.Handle(events)
    return None
