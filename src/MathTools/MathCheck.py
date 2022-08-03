import numpy as np
import sympy as sp
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pygame as pg
from abc import ABC, abstractmethod



def yieldfct():
    yield 1
    yield 2
    yield 3

blah = yieldfct()

blah[0]
