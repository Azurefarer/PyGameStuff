import pygame as pg
import numpy as np
from abc import ABC, abstractmethod

g = 9.8

class Drawer(ABC):

    def draw(self):
        pass

    def draw_data(self):
        pass

class PendulumDraw(Drawer):

    def __init__(self, Win, object):

        self.object = object
        self.Win = Win

    
    def draw(self):

        state = self.object.get_state()
        print('-')
        print(state)
        x = self.object.xaxis + self.object.l * np.sin(state[0])
        y = self.object.yaxis + self.object.l * np.cos(state[0])
                    
        pg.draw.lines(self.Win, self.object.color, False, [(self.object.xaxis, self.object.yaxis), (x, y)], 2)
        pg.draw.circle(self.Win, self.object.color, (x, y), 20)       
        pg.draw.circle(self.Win, (255, 255, 255), (self.object.xaxis, self.object.yaxis), 6)


    def draw_data(self):

        state = self.object.get_state()

        Energy = self.object.get_energy(state)
        
        if len(self.object.data) >= 1500:
            self.object.data.pop(0)
            self.object.data.append(250 - (Energy[1] - Energy[0]) * 1000000000000)
        else:
            self.object.data.append(250 - (Energy[1] - Energy[0]) * 1000000000000)

        #pairing index values with the list values in a new list
        pg.draw.lines(self.Win, (255, 255, 255), False, [(x + 150, y) for x, y in enumerate(self.object.data)], 1)




class DblPendulumDraw(Drawer):

    def __init__(self, Win, object):

        self.object = object
        self.Win = Win

    
    def draw(self):

        state = self.object.get_state()

        x1 = self.object.xaxis + self.object.l1 * np.sin(state[0])
        y1 = self.object.yaxis + self.object.l1 * np.cos(state[0])

        x2 = x1 + self.object.l2 * np.sin(state[1])
        y2 = y1 + self.object.l2 * np.cos(state[1])
                    
        pg.draw.lines(self.Win, self.object.color, False, [(self.object.xaxis, self.object.yaxis), (x1, y1)], 2)
        pg.draw.circle(self.Win, self.object.color, (x1, y1), 20)       
        pg.draw.circle(self.Win, (255, 255, 255), (self.object.xaxis, self.object.yaxis), 6)
        pg.draw.lines(self.Win, self.object.color, False, [(x1, y1), (x2, y2)], 2)
        pg.draw.circle(self.Win, self.object.color, (x2, y2), 20)     


    def draw_data(self):

        state = self.object.get_state()

        Energy = self.object.get_energy(state)
        
        if len(self.object.data) >= 1500:
            self.object.data.pop(0)
            self.object.data.append(50 + (Energy[1] - Energy[0]) * 100000000)
        else:
            self.object.data.append(50 + (Energy[1] - Energy[0]) * 100000000)

        #pairing index values with the list values in a new list
        pg.draw.lines(self.Win, (255, 255, 255), False, [(x + 150, y) for x, y in enumerate(self.object.data)], 1)



class DrawBlock(Drawer):

    def __init__(self, Win, object):

        self.Win = Win
        self.object = object

    def draw(self):
        
        state = self.object.get_state()

        x1 = self.object.x0 + self.object.x
        y1 = self.object.y0 + self.object.y

        pg.draw.circle(self.Win, self.object.color, (x1, y1), 20)       

    def draw_data(self):

        state = self.object.get_state()

        Energy = self.object.get_energy(state)
        
        if len(self.object.data) >= 1500:
            self.object.data.pop(0)
            self.object.data.append(50 + (Energy[1] - Energy[0]) * 100000000)
        else:
            self.object.data.append(50 + (Energy[1] - Energy[0]) * 100000000)

        #pairing index values with the list values in a new list
        pg.draw.lines(self.Win, (255, 255, 255), False, [(x + 150, y) for x, y in enumerate(self.object.data)], 1)

class DrawPlatform(Drawer):

    def __init__(self, Win, object):

        self.Win = Win
        self.object = object

    def draw(self):

        width = self.object.w
        length = self.object.l
        theta = self.object.theta
        off = self.object.offset

        widthx = width * np.sin(theta)
        widthy = width * np.cos(theta)

        x = self.object.x
        xrc = ((length - 2 * off) / 2) * np.cos(theta)
        xlc = ((length + 2 * off) / 2) * np.cos(theta)

        y = self.object.y
        ytc = ((length - 2 * off) / 2) * np.sin(theta)
        ybc = ((length + 2 * off) / 2) * np.sin(theta)

        pg.draw.polygon(self.Win, self.object.color, ([x + xrc + widthx + off, y - ytc + widthy], [x + xrc - widthx + off, y - ytc - widthy], [x - xlc - widthx + off, y + ybc - widthy], [x - xlc + widthx + off, y + ybc + widthy]))
        pg.draw.circle(self.Win, (0, 0, 0), (x + off, y), 12)

    def draw_data(self):

        state = self.object.get_state()

        Energy = self.object.get_energy(state)
        
        #total  energy
        if len(self.object.data) >= 1500:
            self.object.data.pop(0)
            self.object.data.append((Energy[1] - Energy[0]) / 1000)
        else:
            self.object.data.append((Energy[1] - Energy[0]) / 1000)

        #kinetic  energy
        if len(self.object.data1) >= 1500:
            self.object.data1.pop(0)
            self.object.data1.append((Energy[3] - Energy[2]) / 1000)
        else:
            self.object.data1.append((Energy[3] - Energy[2]) / 1000)

        #potential energy
        if len(self.object.data2) >= 1500:
            self.object.data2.pop(0)
            self.object.data2.append((Energy[5] - Energy[4]) / 1000)
        else:
            self.object.data2.append((Energy[5] - Energy[4]) / 1000)
        #pairing index values with the list values in a new list
        #total energy
        pg.draw.line(self.Win, (0, 0, 0), (0, 200), (1800, 200), 1)   
        pg.draw.lines(self.Win, (255, 255, 255), False, [(x + 150, y + 200) for x, y in enumerate(self.object.data)], 1)
   
        #kinetic energy
        pg.draw.line(self.Win, (0, 0, 0), (0, 400), (1800, 400), 1)  
        pg.draw.lines(self.Win, (255, 255, 255), False, [(x + 150, y + 400) for x, y in enumerate(self.object.data1)], 1)

        #potential energy
        pg.draw.line(self.Win, (0, 0, 0), (0, 600), (1800, 600), 1)
        pg.draw.lines(self.Win, (255, 255, 255), False, [(x + 150, y + 600) for x, y in enumerate(self.object.data2)], 1)


