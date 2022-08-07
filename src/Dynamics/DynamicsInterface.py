import numpy as np


class dynamics:

    def set_state(self, s):
        self.state = s

    def get_state(self):
        s = np.array(self.state)

        return s

    def get_state_prime(self, s):
        s_dot = np.array([])

        return s_dot
