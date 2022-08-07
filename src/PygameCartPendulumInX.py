import pygame as pg
import numpy as np
from Dynamics.CartPendulumDynamicsInX import CartPendulumInX
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
    cart_p_inX1 = CartPendulumInX(300, 300, 3, 1, 5, np.deg2rad(0), 900, 500, (200, 200, 200))
    system = System(cart_p_inX1)
    rksystem = RK4(cart_p_inX1)
    dcart_p_inX1 = DrawCartPendulumInX(Win, cart_p_inX1)
    drawsystem = DrawSystem(dcart_p_inX1)
    ctrl = UIcontroller(cart_p_inX1)

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
        #print(a.get_state())
        if counter % max_count == 0:
            clock.tick(60)
            Win.fill((10, 40, 70))
            drawsystem.draw()
            drawsystem.draw_data()
            pg.display.update()
        counter += 1

    pg.quit()
main()
