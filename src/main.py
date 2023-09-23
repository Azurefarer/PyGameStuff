import pygame as pg
from UI import *

pg.init()

#in millimeters
Width, Height = 1800, 1000  
Win = pg.display.set_mode((Width, Height))
FONT = pg.font.SysFont("courier", 64)
pg.display.set_caption("Dynamics")

def main ():
    run = True
    while(run):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
    
        GUI(Win, FONT)

    pg.quit()
    return


main()
