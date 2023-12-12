from turtle import Turtle
import random

color_list = ["red", "orange", "yellow", "green", "light sky blue"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        color_food = random.choice(color_list)
        self.color(color_food)
        self.speed("normal")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
