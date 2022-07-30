import pygame as pg
import numpy as np
from Dynamics.PlatformDynamics import Platform
from MathTools.Integrator import RK4Integrator as RK4
from DrawTools.Draw import *

pg.init()

#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Platform")


def main():
    run = True
    clock = pg.time.Clock()

    a = Platform(20, 500, 5, 900, 500, 100, np.deg2rad(90), (200, 200, 200))

    rka = RK4(a)
    rk = [rka, a]

    dad = DrawPlatform(Win, a)

    counter = 0
    dt = 1/100
    max_count = 50
    torque = 0
    force = 100000

    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                torque = force * rk[1].rcm
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                torque = -force * rk[1].rcm

        #get state, integrate, set state
        rk[1].set_state(rk[0].integrate(rk[1].get_state(), dt), torque)
        torque = 0
        if counter % max_count == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            dad.draw()
            dad.draw_data()
            pg.display.update()
        
        counter += 1

    pg.quit()


main()

