import sys
import pygame as pg
import numpy as np
from Dynamics.BlockDynamics import Block
from MathTools.Integrator import RK4Integrator as RK4
from DrawTools.Draw import *

pg.init()

#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Block")


def main():
    run = True
    clock = pg.time.Clock()
    t = 0

    a = Block(20, 200, 50, 400, 0, (200, 200, 200))

    rka = RK4(a)
    rk = [rka, a]

    dad = DrawBlock(Win, a)

    counter = 0
    dt = 1/100
    max_count = 50

    while run:
        
        t += dt
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        #get state, integrate, set state
        rk[1].set_state(rk[0].integrate(rk[1].get_state(), dt))

        if counter % max_count == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            dad.draw()
            dad.draw_data()
            pg.display.update()

        counter += 1

    pg.quit()


main()

