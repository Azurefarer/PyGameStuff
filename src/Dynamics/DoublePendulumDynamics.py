import numpy as np

g = 9.8

class DblPendulum:


    def __init__(self, x, y, l1, l2, m1, m2, theta1, theta2, color):

        self.debug = True
        self.xaxis = x
        self.yaxis = y
        self.l1 = l1
        self.l2 = l2
        self.m1 = m1
        self.m2 = m2
        self.color = color
        self.state = [theta1, theta2, 0, 0]
        self.state0 = [theta1, theta2, 0, 0]
        # self.theta1 = theta1
        # self.theta10 = theta1
        # self.theta_dot1 = 0
        # self.theta_dot10 = 0
        # self.theta2 = theta2
        # self.theta20 = theta2
        # self.theta_dot2 = 0
        # self.theta_dot20 = 0
        self.data = [50]
        

    def set_state(self, x):


        self.state = x


    def get_state(self):

        x = np.array(self.state)

        return x


    def get_state_prime(self, x):

        z = 0.03
        f1 = -(self.m2 * self.l2 * x[3]**2 * np.sin(x[0] - x[1]) + g * np.sin(x[0]) * (self.m1 + self.m2)) / ((self.m1 + self.m2) * self.l1)
        f2 = (self.l1 * x[2]**2 * np.sin(x[0] - x[1]) - g * np.sin(x[1])) / self.l2
        alpha1 = (self.m2 * self.l2 * np.cos(x[0] - x[1])) / ((self.m1 + self.m2) * self.l1)
        alpha2 = (self.l1 / self.l2) * np.cos(x[0] - x[1])

        x_dot = [x[2], x[3], (f1 - alpha1 * f2) / (1 - alpha1 * alpha2), (f2 - alpha2 * f1) / (1 - alpha1 * alpha2)]

        return x_dot

    def get_state_size(self):
        return 4

    def get_energy(self, x):

        E0 = ((.5 * (self.m1 * (self.l1 * self.state0[2])**2 + self.m2 * ((self.l1 * self.state0[2])**2 + (self.l2 * self.state0[3])**2 + 2 * self.l1 * self.l2 * self.state0[2] * self.state0[3] * np.cos(self.state0[0] - self.state0[1])))
             - g * ((self.m1 + self.m2) * self.l1 * np.cos(self.state0[0]) + self.m2 * self.l2 * np.cos(self.state0[1]))))

        E = ((.5 * (self.m1 * (self.l1 * x[2])**2 + self.m2 * ((self.l1 * x[2])**2 + (self.l2 * x[3])**2 + 2 * self.l1 * self.l2 * x[2] * x[3] * np.cos(x[0] - x[1])))
             - g * ((self.m1 + self.m2) * self.l1 * np.cos(x[0]) + self.m2 * self.l2 * np.cos(x[1]))))

        return E, E0
