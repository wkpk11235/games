targeted_framerate=100

import pygame,math
pygame.init()
clock=pygame.time.Clock()

scrx,scry=800,600

scrwidth,scrheight=scrx,scry

screen=pygame.display.set_mode((scrx,scry))

myfont = pygame.font.SysFont('Comic Sans MS', 30)

inputz=[]

def get_input(): #I made this for myself lol
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
        elif event.type == pygame.KEYDOWN:
            inputz.append(pygame.key.name(event.key))
        elif event.type  == pygame.KEYUP:
            inputz.remove(pygame.key.name(event.key))

class Player():
    def __init__(self,image,x,y,speed=1,image_scale=1):
        self.image=pygame.transform.rotozoom(pygame.image.load(image),0,image_scale)
        self.x=x
        self.y=y
        self.width,self.height=self.image.get_size()
        self.blitx=scrwidth/2+x-self.width/2
        self.blity=scrheight/2-y-self.height/2
    def MoveTo(self,x,y):
        self.blitx=scrwidth/2+x-self.width/2
        self.blity=scrheight/2-y-self.height/2
        self.x=x
        self.y=y
    def Move(self,x,y):
        self.MoveTo(self.x+x,self.y+y)
    def Blit(self,screen):
        screen.blit(self.image,(self.blitx,self.blity))

boi=Player("sans.png",-scrwidth/2,0,image_scale=0.5)

def t(wl,til):
    for i in range(len(wl)):
        if st==til[i]*targeted_framerate:
            global textsurface
            textsurface = myfont.render(wl[i], False, (0, 0, 0))
            return 0

wordl=["hi","im snas","asns teh skselton","bie","bie bie","hav bed tomm"]
timel=[1,2,3,4,5,6]

textsurface = myfont.render('', False, (0, 0, 0))

st=0
while True:
    st+=1
    screen.fill((255,255,255))
    t(wordl,timel)
    get_input()
    if st<(len(timel)+1)*targeted_framerate:
        boi.Move(1,0)
    elif st==(len(timel)+1)*targeted_framerate:
        pygame.mixer.music.load("MegalovaniaMeme.mp3")
        pygame.mixer.music.play(-1)
    else:
        boi.MoveTo(math.sin(st*100)*scrwidth/2,math.cos(st)*scrheight/2)
    screen.blit(textsurface,(boi.blitx,boi.blity-50))
    boi.Blit(screen)
    pygame.display.flip()
    clock.tick(targeted_framerate)
