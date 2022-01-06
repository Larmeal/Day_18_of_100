#สร้างผลงานศิลปะ Damien Hirst

from turtle import Turtle, Screen, colormode
import random
import turtle as t

timmy = Turtle()
timmy.hideturtle()
timmy.shape("turtle")
timmy.speed("fastest")
t.colormode(255)

colors = [[233, 239, 246],
[246, 239, 242], 
[240, 246, 243],
[132, 166, 205],
[221, 148, 106],
[32, 42, 61],
[199, 135, 148], 
[166, 58, 48],
[141, 184, 162],
] 

def random_color():
    test = random.choice(colors)
    r = test[0]
    g = test[1]
    b = test[2]
    color = (r, g, b)
    return color

def paint_color():
    timmy.color(random_color())
    for i in range(0, 10):
        timmy.setheading(0)
        timmy.circle(2)

def move():
    for n in range(0, 10):
        y = n * 60
        timmy.penup()
        timmy.goto(-350, -280 + y)
        for i in range(0, 10):
            timmy.pensize(30)
            timmy.pendown()
            paint_color()
            timmy.penup()
            timmy.forward(75)

move()

screen = Screen()
screen.exitonclick()

# My teacher version