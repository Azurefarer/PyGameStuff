import pygame as pg
import numpy as np
from Dynamics.PendulumDynamics import Pendulum
from Dynamics.System import System
from MathTools.Integrator import RK4Integrator as RK4
from DrawTools.Draw import *
from DrawTools.DrawSystem import *
from Game.Controls import *

pg.init()


#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Pendulum")

g = 9.8
        

def main():
    run = True
    clock = pg.time.Clock()

    #init objects, system, integrator, drawers, system drawer, and controller
    a = Pendulum(300, 300, 400, 1, np.deg2rad(90), (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))
    b = Pendulum(900, 500, 500, 1, np.deg2rad(90), (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))
    c = Pendulum(1500, 300, 400, 1, np.deg2rad(90), (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))
    system = System(a, b, c)

    rksystem = RK4(system)

    da = PendulumDraw(Win, a)
    db = PendulumDraw(Win, b)
    dc = PendulumDraw(Win, c)
    drawsystem = DrawSystem(da, db, dc)

    ctrl = UIcontroller(a, b, c)

    #frame rate and efficiency stuff
    counter = 0
    max_count = 50
    dt = 1/100

    while run:

        #get inputs to influence sim
        ctrlr = ctrl.inputs()
        if ctrlr == 0:
            run = False

        #entire dynamic integration process
        system.set_state(rksystem.integrate(system.get_state(), dt))

        if counter % max_count == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            drawsystem.draw()
            drawsystem.draw_data()
            pg.display.update()

        counter += 1

    pg.quit()


main()
