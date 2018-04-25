import pygame
from scripts import objects

#a="map_data\\"+input("NEW filename:?\n")+".py"
a="maps\\map_data\\"+input("NEW filename:?\n")+".py"

fileboi=open(a,"w")

screen=pygame.display.set_mode((800,600))

draws=[]

actual_data=[]

loaded_images=[]

mousedown=False
deleter=False

now_type="b"
image_type="brick.png"

image=pygame.image.load("images\\"+image_type)
width,height=image.get_size()
loaded_images.append((image,now_type,image_type))

dascript=None

while True:
    print(".",end="")
    screen.fill((255,255,255))
    mousex,mousey=pygame.mouse.get_pos()
    mx=round((mousex-width/2)/width)*width
    my=round((mousey-height/2)/height)*height
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            mousedown=True
        elif event.type==pygame.MOUSEBUTTONUP:
            mousedown=False
        elif event.type==pygame.KEYDOWN:
            tempkey=pygame.key.name(event.key)
            if tempkey=="space":
                deleter=True
            elif tempkey=="o":
                image_type=input("input sprite name:\n")
                now_type=input("input b for brick,p for portal, t for tile, and P for player\n")
                image=pygame.image.load("images\\"+image_type)
                width,height=image.get_size()
                loaded_images.append((image,now_type,image_type))
                if now_type=="t":
                    dascript=input("Input script name.\n")
                    somefile=open("scripts\\tile_scripts\\"+dascript+".py","a+")
                    somefile.close()
            elif tempkey=="s":
                fileboi.write("data="+str(actual_data))
                fileboi.flush()
                print("File Saved Successfully.")
        elif event.type==pygame.KEYUP:
            if pygame.key.name(event.key)=="space":
                deleter=False
    if mousedown:
        if (image,mx,my) not in draws:
            draws.append((image,mx,my))
            if now_type=="p":
                temp=input("Leads to what map?\n")
                actual_data.append([now_type,image_type,mx-400+width/2,300-my-height/2,temp])
            elif now_type=="t":
                actual_data.append([now_type,image_type,mx-400+width/2,300-my-height/2,dascript])
            else:
                actual_data.append([now_type,image_type,mx-400+width/2,300-my-height/2])
    elif deleter:
        for i in loaded_images:
            try:
                rem_ind=draws.index((i[0],mx,my))
                draws.pop(rem_ind)
                actual_data.pop(rem_ind)
            except:
                pass

    pygame.draw.rect(screen,(255,0,0),(mx,my,width,height))

    for i in draws:
        screen.blit(i[0],i[1:])

    pygame.display.flip()
