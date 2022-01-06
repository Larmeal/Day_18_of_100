#หัดใช้ GUI โดยการให้เต่า เดินเป็นจุด ๆ

from turtle import Turtle, Screen, right
import turtle

timmy = Turtle()
timmy.shape("turtle")

for i in range(0, 51):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)







screen = Screen()
screen.exitonclick()