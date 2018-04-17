##needed.
from data import *
##needed.

import math

def start():
    global spawntimer,objects
    spawntimer=0
    objects=[]


def Update():
    global spawntimer
    if spawntimer%5==0:
        bullet=Bullet(0,0,10,10)
        bullet.SetVar('angle',0)
        bullet.SetVar('radius',0)
        objects.append(bullet) ##for recognition

    for bullet in objects:
        angle=bullet.GetVar('angle')
        radius=bullet.GetVar('radius')
        bullet.MoveTo(math.cos(angle)*radius,math.sin(angle)*radius)
        bullet.SetVar('angle',angle+math.pi/32)
        bullet.SetVar('radius',radius+1)


    spawntimer+=1
    return None
