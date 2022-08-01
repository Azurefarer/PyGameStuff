import pygame as pg
from abc import ABC, abstractmethod

pg.init()

class Inputs:

    def playerInputsGet():

        inputsFalse = [False,False,False,False,False,False,False,False,False,False]
        inputs = inputsFalse
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    print("Pressed ESC")
                    inputs[0] = True
                elif event.key == pg.K_UP:
                    inputs[1] = True
                elif event.key == pg.K_DOWN:
                    inputs[2] = True
                elif event.key == pg.K_LEFT:
                    inputs[3] = True
                elif event.key == pg.K_RIGHT:
                    inputs[4] = True
                elif event.key == pg.K_RIGHTBRACKET:
                    inputs[5] = True
                elif event.key == pg.K_LEFTBRACKET:
                    inputs[6] = True
                elif event.key == pg.K_z:
                    inputs[7] = True
                elif event.key == pg.K_F11:
                    inputs[8] = True
                elif event.key == pg.K_x:
                    inputs[9] = True
            return inputs
        try:
            inputs	
            return inputs
        except:
            #print("no inputs to return")
            return inputsFalse

