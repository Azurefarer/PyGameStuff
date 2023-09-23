import numpy as np

g = 9.8

class Block:

    def __init__(self, mass, l, w, x, y, color):
        self.mass = mass
        self.l = l
        self.w = w
        self.color = color

        self.state = [0, 0, 0, 0]
        self.state0 = [x, y, 0, 0]

    # methods for the integrator
    def set_state(self, s):
        self.state = s

    def get_state(self):
        s = np.array(self.state)

        return s

    def get_state_prime(self, s):
        s_dot = np.array([s[2], s[3], 0, g]) # (velX, velY, accX, accY)

        return s_dot

    # inspector methods for drawing
    def get_energy(self, s):
        E0 = self.mass * g * (1000 - self.state0[1]) + .5 * self.mass * self.state0[3] ** 2

        E = self.mass * g * (1000 - s[1]) + .5 * self.mass * s[3] ** 2

        return E, E0

    def get_state0(self):
        return self.state0

    def get_length(self):
        return self.l

    def get_width(self):
        return self.w

    def get_mass(self):
        return self.mass

    def get_color(self):
        return self.color

    # inspector method for the system
    def get_state_size(self):
        return len(self.state)

    # method for the controller
    def impulse(self, direction):
        pass
