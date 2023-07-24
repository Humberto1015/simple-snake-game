from turtle import Turtle
from config import *

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, TOP_BOUND - 10)
        self.hideturtle()
        self.update()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
    
    def update(self):
        self.write(f"Score = {self.score}", move=False, align='center', font=('Arial', 20))
    
    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 20))
