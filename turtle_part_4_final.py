#ให้เต่าหมุนเป็นวงกลม และสุ่มสี

from turtle import Turtle, Screen, colormode
import random
import turtle as t

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
t.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    set_colors = (r, g, b)
    return set_colors

for i in range(0, 361, 5):
    timmy.color(random_colors())
    timmy.setheading(i + 20)
    timmy.circle(100)

screen = Screen()
screen.exitonclick()

# My teacher version

# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# ########### Challenge 5 - Spirograph ########

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)


