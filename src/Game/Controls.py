import pygame as pg
from abc import ABC, abstractmethod

pg.init()

class Animal(ABC):
    def __init__(self):
        pass
    def thing(self):
        print("I am an animal")
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
 
class Snake(Animal):
    def move(self):
        print("I can crawl")
 
class Dog(Animal):
    def move(self):
        print("I can bark")
 
class Lion(Animal):
    def move(self):
        print("I can roar")
 
animals = [Human(), Snake(), Dog(), Lion()]

for animal in animals:
    animal.move()
    animal.thing()
