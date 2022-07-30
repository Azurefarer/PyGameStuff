import sys
import pygame as pg
import numpy as np
from Dynamics.PendulumDynamics import Pendulum
from Dynamics.DoublePendulumDynamics import DblPendulum
from Dynamics.System import System
from MathTools.Integrator import RK4Integrator as RK4
from DrawTools.Draw import *

pg.init()


#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Pendulum")

g = 9.8
        

def main():
    run = True
    clock = pg.time.Clock()
    t = 0

    a = Pendulum(400, 1, np.deg2rad(90), (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))
    b = Pendulum(500, 1, np.deg2rad(90), (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))
    c = Pendulum(600, 1, np.deg2rad(90), (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))

    system = System(a, b, c)

    rksystem = RK4(system)

    # rka = RK4(a)
    # rkb = RK4(b)
    # rkc = RK4(c)

    # rk = [[rka, a], [rkb, b], [rkc, c]]

    da = PendulumDraw(Win, a)
    db = PendulumDraw(Win, b)
    dc = PendulumDraw(Win, c)

    d = [da, db, dc]

    counter = 0
    max_count = 50
    dt = 1/100

    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        system.set_state(rksystem.integrate(system.get_state(), dt))

        # for rk4 in rk:

        #     #get state, integrate, set state
        #     rk4[1].set_state(rk4[0].integrate(rk4[1].get_state(), dt))

        if counter % max_count == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            
            for paint in d:
                paint.draw()
                paint.draw_data()
            pg.display.update()

            # print(a.get_energy(a.get_state()))
            # print(a.get_state())

        counter += 1

    pg.quit()


main()
