import pygame as pg
import PygameDblPendulum

pg.init()

def GUI(Window, font):

    DynamicsTxt = font.render("Dynamics", 1, (200, 200, 200))
    Window.blit(DynamicsTxt, (25, 25))    

    pg.draw.rect(Window, (255, 255, 255), ((25, 100), (600, 125)), width = 1)
    DblPendTxt = font.render("Double Pendulum", 1, (200, 200, 200))
    Window.blit(DblPendTxt, (25, 120)) 
    if pg.mouse.get_pos()[0] > 25 and pg.mouse.get_pressed()[0] and pg.mouse.get_pos()[0] < 600:
        pg.display.set_caption("DoublePendulum")
        PygameDblPendulum.main(Window)
        print("box clicked")

    pg.display.update()