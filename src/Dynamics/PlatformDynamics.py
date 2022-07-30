import numpy as np


g = 9.8


class Platform:

    def __init__(self, mass, l, w, x, y, offset, theta, color):

        self.mass = mass
        self.l = l
        self.w = w
        self.x = x
        self.x0 = x
        self.y = y
        self.y0 = y
        self.offset = offset
        self.theta = theta
        self.theta0 = theta
        self.theta_dot = 0
        self.theta_dot0 = 0
        self.color = color

        self.torque = 0
        #moment of inertia
        self.I = (1/12) * mass * l**2 + mass * offset**2
        
        #right and left center of mass
        self.rcm = (l - 2 * offset) / 4
        self.lcm = (l + 2 * offset) / 4
        #right and left offset ratio
        self.rof = (l - 2 * offset) / (l * 2)
        self.lof = (l + 2 * offset) / (l * 2)

        self.data = [0]
        self.data1 = [0]
        self.data2 = [0]


    def set_state(self, s, torque):

        self.theta = s[0]
        self.theta_dot = s[1]
        self.torque = torque


    def get_state(self):

        s = np.array([self.theta, self.theta_dot])

        return s


    def get_state_prime(self, s):

        #gravity acting on the center of mass
        taug = self.mass * g * self.offset
        #user input torque
        taup = self.torque

        s_dot = np.array([s[1], ((taup + taug * np.sin((np.pi / 2) - s[0])) / self.I)])
        
        return s_dot


    def get_energy(self, s):

        E0 = .5 * self.I * self.theta_dot0**2 - self.offset * g * self.mass * np.sin(self.theta0)

        E = .5 * self.I * s[1]**2 - self.offset * g * self.mass * np.sin(s[0])

        KE0 = .5 * self.I * self.theta_dot0**2

        KE = .5 * self.I * s[1]**2

        U0 = - self.offset * g * self.mass * np.sin(self.theta0)

        U = - self.offset * g * self.mass * np.sin(s[0])

        return E, E0, KE, KE0, U, U0
