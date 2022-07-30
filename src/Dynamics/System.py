import numpy as np
from Dynamics.DynamicsInterface import Object

class System(Object):

    def __init__(self, *args):
        
        self.args = args

    def set_state(self, x):
        
        j = self.args[0].get_state_size()
        for i in range(len(self.args)):
            self.args[i].set_state(x[j-self.args[i].get_state_size():j])
            j += self.args[i].get_state_size()
        

    def get_state(self):

        x = []
        for i in range(len(self.args)):
            for j in range(self.args[i].get_state_size()):
                x.append(self.args[i].get_state()[j])
        return np.array(x)

    def get_state_prime(self, x):
        k = 0
        print(x)
        x_dot = []
        for object in self.args:

            state_slice = x[k:k + object.get_state_size()]
            print(state_slice)
            object_state = object.get_state_prime(state_slice)
            x_dot = x_dot + object_state
            k += object.get_state_size()

        return np.array(x_dot)


    def get_state_size(self):

        size = 0
        for i in range(len(self.args)):
            size += self.args[i].get_state_size()

        return size
