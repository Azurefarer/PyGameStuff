import pygame as pg
import numpy as np
from sympy import blockcut
from Dynamics.PlatformDynamics import Platform
from Dynamics.BlockDynamics import Block
from Dynamics.System import System
from MathTools.Integrator import RK4Integrator as RK4
from DrawTools.Draw import *
from DrawTools.DrawSystem import *
from Game.Controls import *

pg.init()

#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
pg.display.set_caption("Platform")


def main():
    run = True
    clock = pg.time.Clock()

    #init platform, system, integrator, drawer, and controller
    a = Platform(200, 500, 5, 900, 500, 0, np.deg2rad(0), (200, 200, 200))
    block = Block(1, 20, 30, 800, 400, (165, 89, 54))
    system = System(a, block)
    rksystem = RK4(system)
    da = DrawPlatform(Win, a)
    dblock = DrawBlock(Win, block)
    drawsystem = DrawSystem(da, dblock)
    ctrl = UIcontroller(a, block)

    #framerate and efficiency stuff
    dt = 1/100
    counter = 0
    max_count = 50

    while run:
        
        #get inputs to influence sim
        ctrlr = ctrl.inputs()
        if ctrlr == 0:
            run = False

        #get state, integrate, set state
        #set state also reverts changes from inputs
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

