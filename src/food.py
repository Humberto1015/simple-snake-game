from turtle import Turtle
from config import *
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        new_x = random.randint(LEFT_BOUND + 20, RIGHT_BOUND - 20)
        new_y = random.randint(BOTTOM_BOUND + 20, TOP_BOUND - 20)
        self.goto(new_x, new_y)
    