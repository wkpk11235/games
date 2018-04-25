if 1: #un make later bruh
    targeted_framerate=100
    import pygame,os,sys
    pygame.init()
    boi=None
    from scripts import objects
    sys.path.insert(0, os.path.dirname(sys.argv[0])+"\\maps\\") ##da fuge
    playing=True
    events=[]
    scrwidth,scrheight=800,600
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((scrwidth,scrheight))
    pygame.display.set_caption('OVERDRIVE')
    pygame.display.set_icon(pygame.image.load("images\\ovrdrv.png"))
    objects.scrwidth=scrwidth
    objects.scrheight=scrheight

def handle_input(): #I made this for myself lol
    global playing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False
        elif event.type == pygame.KEYDOWN:
            events.append(pygame.key.name(event.key))
        elif event.type == pygame.KEYUP:
            events.remove(pygame.key.name(event.key))

from maps import map001

curmap=map001
objects.allobjs=[]
map001.players=[]
map001.portals=[]
map001.bricks=[]
map001.tiles=[]
map001.Init()
for obj in map001.map_ext.data:
    if obj[0]=="P":
        map001.players.append(objects.Player(obj[1],obj[2],obj[3]))
    elif obj[0]=="b":
        map001.bricks.append(objects.Brick(obj[1],obj[2],obj[3]))
    elif obj[0]=="p":
        map001.portals.append(objects.Portal(obj[1],obj[2],obj[3],obj[4]))
    elif obj[0]=="t":
        map001.tiles.append(objects.Tile(obj[1],obj[2],obj[3]))

while playing:
    screen.fill((255,255,255))
    handle_input()
    for plr in curmap.players:
        plr.Handle(events)
    for prtls in curmap.portals:
        if prtls.checkplayer()==True:
            boi=__import__(prtls.leadsto)
    da=curmap.Update(events)
    if da!=None or boi!=None:
        if da!=None:
            curmap=da
        else:
            curmap=boi
            boi=None
            da=curmap
        objects.allobjs=[]
        da.players=[]
        da.portals=[]
        da.bricks=[]
        da.tiles=[]
        da.Init()
        for obj in da.map_ext.data:
            if obj[0]=="P":
                da.players.append(objects.Player(obj[1],obj[2],obj[3]))
            elif obj[0]=="b":
                da.bricks.append(objects.Brick(obj[1],obj[2],obj[3]))
            elif obj[0]=="p":
                da.portals.append(objects.Portal(obj[1],obj[2],obj[3],obj[4]))
            elif obj[0]=="t":
                da.tiles.append(objects.Tile(obj[1],obj[2],obj[3],obj[4]))
    for obj in objects.allobjs:
        obj.Blit(screen)
    pygame.display.flip()
    clock.tick(targeted_framerate)
