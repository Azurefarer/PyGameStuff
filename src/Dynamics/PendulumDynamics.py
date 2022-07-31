import numpy as np

g = 9.8

class Pendulum:

    def __init__(self, x, y, l, m, theta, color):

        self.xaxis = x
        self.yaxis = y
        self.l = l
        self.m = m
        self.color = color    

        self.state = [theta, 0]
        self.state0 = [theta, 0]
        

    def set_state(self, x):

        self.state = x


    def get_state(self):

        x = np.array(self.state)

        return x


    def get_state_prime(self, x):

        z = 0.0
        w = np.sqrt(g/self.l)
        x_dot = np.array([x[1], -(w**2) * np.sin(x[0]) - 2 * z * w * x[1]])

        return x_dot



    def get_energy(self, x):

        E0 = .5 * self.m * (self.state0[1] * self.l)**2 - g * self.m * self.l * np.cos(self.state0[0])

        E = .5 * self.m * (x[1] * self.l)**2 - g * self.m * self.l * np.cos(x[0])

        return E, E0


    def get_state_size(self):
        return 2

    def get_axis(self):
        return self.xaxis, self.yaxis

    def get_length(self):
        return self.l

    def get_mass(self):
        return self.m

    def get_color(self):
        return self.color

    