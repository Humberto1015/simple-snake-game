from turtle import Turtle
from config import *

class Snake:
    def __init__(self, init_len):
        self.segments = []
        self.curr_len = init_len
        self.init_snake()
        self.head = self.segments[0]
        
    def init_snake(self):
        for idx in range(self.curr_len):
            segment = self.create_new_segment(STARTING_POSITION[0] - idx * MOVE_DISTANCE, STARTING_POSITION[1])
            self.segments.append(segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for idx in range(self.curr_len - 1, 0, -1):
            next_position = self.segments[idx - 1].pos()
            self.segments[idx].goto(next_position)
        self.head.forward(MOVE_DISTANCE)

    def create_new_segment(self, start_x, start_y):
        segment = Turtle('square')
        segment.speed('fastest')
        segment.color('white')
        segment.penup()
        segment.goto(start_x, start_y)
        return segment
    
    def add_one_segment(self):
        tail_pos = self.segments[-1].pos()
        segment = self.create_new_segment(tail_pos[0] - MOVE_DISTANCE, tail_pos[1])
        self.segments.append(segment)
        self.curr_len += 1