import pygame as pg
import numpy as np
from Dynamics.DoublePendulumDynamics import DblPendulum
from MathTools.Integrator import RK4Integrator as RK4
from DrawTools.Draw import *
from DrawTools.DrawSystem import *
from Dynamics.System import System
from Game.Controls import *

pg.init()



g = 9.8


def main(Win):
    run = True
    clock = pg.time.Clock()

    # init objects, system, integrator, drawers, system drawer, and controller
    ad = DblPendulum(900, 200, 300, 400, 1, 1, np.deg2rad(120), np.deg2rad(60), (200, 200, 200))
    system = System(ad)
    rksystem = RK4(ad)

    dad = DblPendulumDraw(Win, ad)
    drawsystem = DrawSystem(dad)

    ctrl = UIcontroller(ad)

    # framerate eand efficieny stuff
    counter = 0
    dt = 1 / 100
    max_count = 50

    while run:

        # get inputs to influence sim
        ctrlr = ctrl.inputs()
        if ctrlr == 0:
            run = False

        # entire dynamic integration process
        system.set_state(rksystem.integrate(system.get_state(), dt))

        if counter % max_count == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            drawsystem.draw()
            drawsystem.draw_data()
            pg.display.update()

        counter += 1

    pg.quit()


