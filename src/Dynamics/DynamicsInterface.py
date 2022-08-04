import numpy as np
from abc import ABC, abstractmethod


class Object(ABC):

    def set_state(self, x):
        pass

    def get_state(self):
        pass

    def get_state_prime(self, x):
        pass
