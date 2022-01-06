# ให้เต่า เดินสุ่มพร้อมกับวาดสีไปด้วย

from turtle import Turtle, Screen, back, backward, right
import random

timmy = Turtle()
timmy.shape("turtle")

def random_timmy():
    number = [1, 2, 3, 4]
    random_number = random.choice(number)
    if random_number == 1:
        timmy.forward(20)
    elif random_number == 2:
        timmy.back(20)
    elif random_number == 3:
        timmy.left(90)
        timmy.forward(20)
    elif random_number == 4:
        timmy.right(90)
        timmy.forward(20)

def random_color():
    colors = ["blue", "red", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    random_timmy_colors = random.choice(colors)
    timmy.color(random_timmy_colors)

for i in range(100):
    random_color()
    random_timmy()

screen = Screen()
screen.exitonclick()

# My teacher version

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")

# for _ in range(200):
#     timmy.color(random.choice(colours))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))