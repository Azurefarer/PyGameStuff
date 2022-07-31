import numpy as np
from Dynamics.DynamicsInterface import Object

class System(Object):

    def __init__(self, *args):
        
        self.args = args

    def set_state(self, x):
        
        j = 0
        for object in self.args:
            object.set_state(x[j:j + object.get_state_size()])
            j += object.get_state_size()
        

    def get_state(self):
        x = []
        for object in self.args:
            for j in range(object.get_state_size()):
                x.append(object.get_state()[j])
        return np.array(x)


    def get_state_prime(self, x):
        k = 0
        x_dot = np.array([])
        for object in self.args:

            state_slice = x[k:k + object.get_state_size()]
            object_state = object.get_state_prime(state_slice)
            x_dot = np.concatenate((x_dot, object_state))
            k += object.get_state_size()

        return np.array(x_dot)


    def get_state_size(self):

        size = 0
        for i in range(len(self.args)):
            size += self.args[i].get_state_size()

        return size
