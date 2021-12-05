import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
import random

color_list = [(222, 231, 237), (239, 74, 34), (6, 148, 93), (231, 238, 234), (232, 168, 40),
              (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93),
              (172, 36, 98),(246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26), (235, 164, 190),
              (156, 25, 22), (20, 189, 230), (238, 169, 157), (162, 210, 182), (137, 211, 232), (0, 123, 53),
              (85, 131, 185), (181, 187, 212), (243, 13, 24)]

tim = Turtle()
tim.shape('turtle')
tim.speed('fastest')
tim.hideturtle()
screen = Screen()
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()