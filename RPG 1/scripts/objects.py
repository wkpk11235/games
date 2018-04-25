import pygame,sys,os
pygame.init()

scrwidth=800
scrheight=600

objs=[]
allobjs=[]
tiles=[]

player=None

sys.path.insert(0, os.path.dirname(sys.argv[0])+"\\scripts\\tile_scripts") ##da fuge

class AllObject():
    def __init__(self,image,x,y):
        self.image=pygame.image.load("images\\"+image)
        self.x=x
        self.y=y
        self.width,self.height=self.image.get_size()
        self.rect=self.image.get_rect()
        self.rect.x=scrwidth/2+x-self.width/2
        self.rect.y=scrheight/2-y+self.height/2
        allobjs.append(self)
    def Safe_MoveTo(self,x,y):
        oldx=self.rect.x
        oldy=self.rect.y
        self.rect.x=scrwidth/2+x-self.width/2
        self.rect.y=scrheight/2-y+self.height/2
        if (self.rect.collidelist(objs)==-1):
            self.x=x
            self.y=y
        else:
            self.rect.x=oldx
            self.rect.y=oldy
    def Safe_Move(self,x,y):
        self.Safe_MoveTo(self.x+x,self.y+y)
    def MoveTo(self,x,y):
        self.rect.x=scrwidth/2+x-self.width/2
        self.rect.y=scrheight/2-y-self.height/2
        self.x=x
        self.y=y
    def Move(self,x,y):
        self.MoveTo(self.x+x,self.y+y)
    def Blit(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        pygame.draw.rect(screen,(255,0,0),(self.rect.x,self.rect.y,self.rect.width,self.rect.height),1)

class Player():
    def __init__(self,image,x,y,speed=1):
        self.image=pygame.image.load("images\\"+image)
        self.x=x
        self.y=y
        self.width,self.height=self.image.get_size()
        self.hwd=self.height-self.width
        self.rect=self.image.get_rect()
        self.rect.x=scrwidth/2+x-self.width/2
        self.rect.y=scrheight/2-y+self.height/2+self.hwd
        self.rect.height=self.rect.width
        self.rect.h=self.rect.w
        allobjs.append(self)
        global player
        self.enable_movement=True
        self.speed=speed
        player=self
    def Safe_MoveTo(self,x,y):
        oldx=self.rect.x
        oldy=self.rect.y
        self.rect.x=scrwidth/2+x-self.width/2
        self.rect.y=scrheight/2-y-self.height/2+self.hwd
        if (self.rect.collidelist(objs)==-1):
            self.x=x
            self.y=y
        else:
            self.rect.x=oldx
            self.rect.y=oldy
    def Safe_Move(self,x,y):
        self.Safe_MoveTo(self.x+x,self.y+y)
    def Handle(self,events):
        if self.enable_movement:
            for event in events:
                if event=="up":
                    self.Safe_Move(0,self.speed)
                if event=="down":
                    self.Safe_Move(0,-self.speed)
                if event=="right":
                    self.Safe_Move(self.speed,0)
                if event=="left":
                    self.Safe_Move(-self.speed,0)
    def Blit(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y-self.hwd))
        pygame.draw.rect(screen,(255,0,0),(self.rect.x,self.rect.y,self.rect.width,self.rect.height),1)

class Brick(AllObject):
    def __init__(self,image,x,y):
        #super(AllObject, self).__init__()
        AllObject.__init__(self,image,x,y)
        objs.append(self.rect)
class Portal(AllObject):
    def __init__(self,image,x,y,leadsto):
        #super(AllObject, self).__init__()
        AllObject.__init__(self,image,x,y)
        self.leadsto=leadsto
    def checkplayer(self):
        if self.rect.colliderect(player.rect):
            return True
        return None
class Tile(AllObject):
    def __init__(self,image,x,y,script):
        AllObject.__init__(self,image,x,y)
        self.rect.width=0
        self.rect.height=0
        self.rect.w=0
        self.rect.h=0
        if script!=None:
            self.script=__import__(script)
        tiles.append(self)
