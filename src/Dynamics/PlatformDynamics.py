import numpy as np


g = 9.8


class Platform:

    def __init__(self, mass, l, w, x, y, offset, theta, color):
        
        #in kg and m
        self.mass = mass
        self.l = l
        self.w = w
        self.xaxis = x
        self.x0 = x
        self.yaxis = y
        self.y0 = y
        self.offset = offset
        self.state = [theta, 0]
        self.state0 = [theta, 0]

        self.color = color

        self.torque = 0
        #moment of inertia
        self.I = (1/12) * mass * l**2 + mass * offset**2
        
        #right and left center of mass
        self.rcm = (l - 2 * offset) / 4
        self.lcm = (l + 2 * offset) / 4


    #methods for the integrator
    def set_state(self, s):
        
        self.state = s
        self.torque = 0

    def get_state(self):

        s = np.array(self.state)

        return s


    def get_state_prime(self, s):

        #gravity acting on the center of mass
        taug = self.mass * g * self.offset

        #user input torque
        taup = self.torque

        s_dot = np.array([s[1], ((taup + taug * np.sin((np.pi / 2) - s[0])) / self.I)])
        
        return s_dot

    #inspector methods for drawing
    def get_energy(self, s):

        #total energy
        E0 = .5 * self.I * self.state0[1]**2 - self.offset * g * self.mass * np.sin(self.state0[0])

        E = .5 * self.I * s[1]**2 - self.offset * g * self.mass * np.sin(s[0])

        #kinetic energy
        KE0 = .5 * self.I * self.state0[1]**2

        KE = .5 * self.I * s[1]**2

        #potential energy
        U0 = - self.offset * g * self.mass * np.sin(self.state0[0])

        U = - self.offset * g * self.mass * np.sin(s[0])

        return E, E0, KE, KE0, U, U0

    def get_axis(self):
        return self.xaxis, self.yaxis

    def get_length(self):
        return self.l

    def get_width(self):
        return self.w

    def get_offset(self):
        return self.offset

    def get_mass(self):
        return self.mass

    def get_color(self):
        return self.color

    #inspector method for the system
    def get_state_size(self):
        return 2

    #method for the controller
    def impulse(self, direction):
        force = 100000
        forces = [force * -1, force]

        #7500N*m for offset of 100mm
        self.torque = forces[direction] * self.rcm
