import pygame as pg
import numpy as np
from Dynamics.CartPendulumDynamics import CartPendulum
from MathTools.Integrator import RK4Integrator as RK4
from DrawTools.Draw import *
from DrawTools.DrawSystem import *
from Dynamics.System import System
from Game.Controls import *

pg.init()


#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Thing")

g = 9.8


def main():
    run = True
    clock = pg.time.Clock()

    #init objects, system, integrator, drawers, system drawer, and controller
    a = CartPendulum(300, 300, 3, 1, 5, np.deg2rad(0), 900, 500, .01, (200, 200, 200))
    system = System(a)
    rksystem = RK4(a)
    da = DrawCartPendulum(Win, a)
    drawsystem = DrawSystem(da)
    ctrl = UIcontroller(a)

    #framerate and efficieny stuff
    dt = 1/100
    counter = 0
    max_count = 50

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
