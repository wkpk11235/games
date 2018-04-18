##needed.
from game import Bullet
##needed.

import math

def start():
    global spawntimer,objects,mult,debug_text
    spawntimer=0

    objects=[] #you must contain all bullets here
    debug_text=str(globals()) #debug text goes here

    mult=0.5


def Update():
    global spawntimer,mult
    spawntimer = spawntimer + 1
    if(spawntimer % 300 == 0):
        for i in range(1,11):

            bullet = Bullet(0, 180,"s.png")
            bullet.SetVar('timer', 0)
            bullet.SetVar('offset', math.pi * i/5)
            bullet.SetVar('negmult', mult)
            bullet.SetVar('lerp', 0)
            objects.append(bullet)
        mult+=0.05

    for bullet in objects:
        timer = bullet.GetVar('timer')
        offset = bullet.GetVar('offset')
        lerp = bullet.GetVar('lerp')
        posx = (70*lerp)*math.sin(timer*bullet.GetVar('negmult') + offset)
        posy = (70*lerp)*math.cos(timer + offset) + 180 - lerp*50
        bullet.MoveTo(posx, posy)
        bullet.SetVar('timer', timer + 1/40)
        lerp+= 1 / 90
        if lerp > 4:
            lerp=4
        bullet.SetVar('lerp', lerp)
