#initzation
UTcoord=True #ut foreber!!


framerate=60 #best

scrwidth=500; scrheight=500;

import pygame,math,time,os,sys,random

pygame.init()

kaboom = pygame.mixer.Sound('bamm.wav')

pygame.mixer.music.load("tada.ogg")

pygame.mixer.music.play(-1)

clock=pygame.time.Clock()

#here is da module importion stuff

curdir=os.path.dirname(sys.argv[0])
wavedir=curdir+"\\waves"
sys.path.insert(0, wavedir) ##da fuge

sequenced_waves=[]
random_waves=[]

for folder in os.walk(wavedir):
    for files in folder:
        for file in files:
            if file.endswith(".py"):
                if file!="data.py":
                    if file[0]=="_":
                        sequenced_waves.append(__import__(file[:-3]))
                    else:
                        random_waves.append(__import__(file[:-3]))

print("Bullet Dodge V0.1 Press enter to start")
input()

screen = pygame.display.set_mode((scrwidth,scrheight))

pygame.display.set_caption('DODGE')

startime=time.time()

width=10
dx=0
dy=0
px=0
py=scrheight-width
speed=3

inputz=[]


playing=True

def get_input(): #I made this for myself lol
    global playing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False
        elif event.type == pygame.KEYDOWN:
            inputz.append(pygame.key.name(event.key))
        elif event.type  == pygame.KEYUP:
            inputz.remove(pygame.key.name(event.key))


def handle_input():
    global dx
    global dy
    global speed
    local_speed=speed
    local_dx=0
    local_dy=0

    if "left shift" in inputz:
        local_speed=speed+1

    for key in inputz:
        if key=="right":
            local_dx+=local_speed
        elif key=="left":
            local_dx-=local_speed
        if key=="down":
            local_dy+=local_speed
        elif key=="up":
            local_dy-=local_speed
    dx=local_dx
    dy=local_dy


def handle_player():
    global px
    global py
    prx=px+dx
    pry=py+dy
    if prx+width<scrwidth and prx>=0:
        px=prx
    if pry+width<scrheight and pry>=0:
        py=pry


def checktouch(bullet):
    if UTcoord:
        dax=bullet.x+scrwidth/2
        day=scrheight/2-bullet.y
    else:
        dax=bullet.x
        day=bullet.y
    maxpx=px+width
    minpx=px
    maxbx=dax+bullet.width
    minbx=dax
    if (minbx<=minpx<=maxbx or minbx<=maxpx<=maxbx):
        maxpy=py+width
        minpy=py
        maxby=day+bullet.height
        minby=day
        if (minby<=minpy<=maxby or minby<=maxpy<=maxby):
            global playing
            playing=False



timer=0
kill=False
death=False
wavenum=0
dareturn=None

def switchwave():
    global wavenum,dawave
    if len(sequenced_waves)>wavenum:
        dawave=sequenced_waves[wavenum]
        wavenum+=1
    else:
        dawave=random.choice(random_waves)
    dawave.start()

switchwave()

def submain():
    global timer,dareturn,dawave
    timer+=1
    screen.fill((255,255,255))

    if dareturn=="End":
        switchwave()

    get_input()
    handle_input()
    handle_player()

    dareturn = dawave.Update()

    for object in dawave.objects:
        if UTcoord:
            pygame.draw.rect(screen,(0,0,0),(object.x+scrwidth/2,scrheight/2-object.y,object.width,object.height))
        else:
            pygame.draw.rect(screen,(0,0,0),(object.x,object.y,object.width,object.height))
        checktouch(object)

    pygame.draw.rect(screen,(255,0,0),(px,py,width,width))

    if playing:
        pygame.display.flip()
    else:
        kaboom.play()
        pygame.display.quit()
    clock.tick(framerate)



while playing:
    submain()


scorr=(time.time()-startime)

print("You lose. Lasted "+str(scorr)+" seconds.")

if scorr<3000:
    print("I know you can do better!")
elif scorr<10000:
    print("Good, but try harder.")
elif scorr<100000:
    print("You're pretty good!")
else:
    print("NICE!")

input()
