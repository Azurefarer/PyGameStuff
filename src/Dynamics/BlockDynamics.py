import numpy as np

g = 9.8

class Block:

    def __init__ (self, mass, l, w, x, y, color):

        self.mass = mass
        self.l = l
        self.w = w
        self.color = color

        self.x = 0
        self.y = 0
        self.x_dot = 0
        self.y_dot = 0

        self.x0 = x
        self.y0 = y
        self.x_dot0 = 0
        self.y_dot0 = 0

        self.data = [0]

    def set_state(self, s):

        self.x = s[0]
        self.y = s[1]
        self.x_dot = s[2]
        self.y_dot = s[3]


    def get_state(self):

        s = np.array([self.x, self.y, self.x_dot, self.y_dot])

        return s


    def get_state_prime(self, s):

        s_dot = np.array([s[2], s[3], 0, g])

        return s_dot


    def get_energy(self, s):

        E0 = self.mass * g * (1000 - self.y0) + .5 * self.mass * self.y_dot0**2

        E = self.mass * g * (1000 - s[1]) + .5 * self.mass * s[3]**2

        return E, E0