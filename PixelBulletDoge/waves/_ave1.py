##needed.
from game import Bullet
##needed.

import math

def start():
    global spawntimer,objects
    spawntimer=0
    objects=[]
    bullet=Bullet(0,0,"s.png")
    objects.append(bullet)

def Update():
    global spawntimer
    for bullet in objects:
        bullet.MoveTo(math.cos(spawntimer/50)*100,math.sin(spawntimer/50)*100)
    spawntimer+=1
    return None
