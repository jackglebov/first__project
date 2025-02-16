import pygame as py
from random import *
py.init()
speed = 0.1
x=0
FPS=30
win = py.display.set_mode((500, 600))

'''
for i in range(1,100,1):
    x = randint(1, 255)
    z = randint(1, 255)
    c= randint(1, 255)
'''
clock = py.time.Clock()
while True:
    win.fill((255, 255, 255))
    py.draw.circle(win ,(255,0,0),(x,250),24)
    x=x+speed
    py.display.update()
    if x  >500:
        speed=-0.1
    if x < 0:
        speed = 0.1
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
