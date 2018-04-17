class Bullet(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.dict={}
    def Move(self,xinc,yinc):
        self.x+=xinc
        self.y+=yinc
    def MoveTo(self,xpos,ypos):
        self.x=xpos
        self.y=ypos
    def SetVar(self,a,b):
        self.dict[a]=b
    def GetVar(self,a):
        try:
            return self.dict[a]
        except KeyError:
            return None
