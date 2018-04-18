DEBUG=True #launches debugger
framerate=60 #best

import pygame,pixelperfect,os,sys;pygame.init()
scrwidth,scrheight=(500,500)
curdir=os.path.dirname(sys.argv[0])

class Bullet(object):
    def __init__(self,xpos,ypos,image,boxfit=False):
        self.boxfit=boxfit
        self.image=pygame.image.load(curdir+"\\sprites\\"+image)
        self.width, self.height = self.image.get_size()
        self.rect=self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
        self.x=xpos
        self.y=ypos
        self.renderx=xpos+scrwidth/2-self.width/2
        self.rendery=scrheight/2-ypos+self.height/2
        self.hitmask=pixelperfect.get_alpha_hitmask(self.image, self.rect)
        self.dict={}
    def Move(self,dx,dy):
        prx=self.x+dx
        pry=self.y+dy
        if self.boxfit:
            if -scrwidth/2+self.width/2<=prx<=scrwidth/2-self.width/2:
                self.x=prx
                self.renderx=self.x+scrwidth/2-self.width/2
                self.rect.x=self.renderx
            if -scrheight/2+self.height/2<=pry<=scrheight/2-self.height/2:
                self.y=pry
                self.rendery=scrheight/2-self.y-self.height/2
                self.rect.y=self.rendery
        else:
            self.x=prx
            self.renderx=self.x+scrwidth/2-self.width/2
            self.rect.x=self.renderx
            self.y=pry
            self.rendery=scrheight/2-self.y-self.height/2
            self.rect.y=self.rendery
    def MoveTo(self,xpos,ypos):
        self.x=xpos
        self.renderx=self.x+scrwidth/2-self.width/2
        self.rect.x=self.renderx
        self.y=ypos
        self.rendery=scrheight/2-self.y-self.height/2
        self.rect.y=self.rendery


    def SetVar(self,a,b):
        self.dict[a]=b
    def GetVar(self,a):
        try:
            return self.dict[a]
        except KeyError:
            return 0

if __name__=="__main__":
    #initzation

    import math,time,random,tkinter

    kaboom = pygame.mixer.Sound('bamm.wav')

    pygame.mixer.music.load("tada.ogg")

    pygame.mixer.music.play(-1)

    clock=pygame.time.Clock()

    #here is da module importion stuff
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
                local_dy-=local_speed
            elif key=="up":
                local_dy+=local_speed
        dx=local_dx
        dy=local_dy


    def handle_player():
        player.Move(dx,dy)





    player=Bullet(0,0,"sans.png",True)


    timer=0
    kill=False
    death=False
    wavenum=0
    dareturn=None

    def switchwave(): #modify for your own liking
        global wavenum,dawave
        if len(sequenced_waves)>wavenum:
            dawave=sequenced_waves[wavenum]
            wavenum+=1
        else:
            dawave=random.choice(random_waves)
        dawave.start() #initialize wave

    switchwave()

    def render(obj):
        screen.blit(obj.image,(obj.renderx,obj.rendery))
        if DEBUG:
            pygame.draw.rect(screen,(255,0,0),(obj.rect.x,obj.rect.y,obj.width,obj.height),1)


    def submain():
        global timer,dareturn,dawave,playing
        timer+=1
        screen.fill((255,255,255))

        if dareturn=="End":
            switchwave()

        get_input()
        handle_input()
        handle_player()

        dareturn = dawave.Update()

        for object in dawave.objects:
            render(object)
            if pixelperfect.check_collision(object,player):
                playing=False
                break


        render(player)

        if playing:
            pygame.display.flip()
        else:
            kaboom.play()
            pygame.display.quit()
        clock.tick(framerate)

    if DEBUG:
        debugger=tkinter.Tk()
        debugger.geometry("200x100")
        result=tkinter.Label(text="")
        result.pack()


    while playing:
        if DEBUG:
            global dawave
            try:
                result.configure(text=dawave.debug_text)
            except Exception:
                pass
            debugger.update_idletasks()
            debugger.update()
        if pygame.mouse.get_focused()!=0:
            submain()
    if DEBUG:
        debugger.mainloop()
    else:
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
