import pygame
import random

class Food:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Pos(self):
        return self.x, self.y