import pygame as pg
import numpy as np
from Dynamics.PendulumDynamics import Pendulum
from Dynamics.DoublePendulumDynamics import DblPendulum
from Dynamics.BlockDynamics import Block
from Dynamics.PlatformDynamics import Platform
from Dynamics.System import System
from MathTools.Integrator import RK4Integrator as RK4
from DrawTools.DrawSystem import *
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

    #init objects
    a = Pendulum(900, 300, 400, 1, np.deg2rad(90), (100, 200, 0))
    b = Block(1, 5, 5, 600, 0, (80, 75, 230))
    c = Platform(20, 300, 5, 300, 600, 70, np.deg2rad(0), (100, 100, 100))
    d = DblPendulum(900, 500, 200, 300, 1000, 10, np.deg2rad(180.1), np.deg2rad(180), (200, 200, 200))

    #init system of objects

    system = System(a, b, c, d)

    #init integrator for the system
    rksystem = RK4(system)

    #init drawers
    da = PendulumDraw(Win, a)
    db = DrawBlock(Win, b)
    dc = DrawPlatform(Win, c)
    dd = DblPendulumDraw(Win, d)
 
    #init system drawing
    drawsystem = DrawSystem(da, dd)


    #frame rate and efficiency stuff
    counter = 0
    max_count = 60
    dt = 1/100

    while run:

        #press exit in top right
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        #entire dynamic integration process
        system.set_state(rksystem.integrate(system.get_state(), dt))

        #drawing and frame rate methods
        if counter % max_count == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            drawsystem.draw()
            drawsystem.draw_data()
            pg.display.update()

        counter += 1

    pg.quit()


main()
