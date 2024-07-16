import colorgram
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
colors = colorgram.extract('Hirst-Painting/image.jpg', 30)
screen = Screen()

colors_list = []

for i in colors:
  r = i.rgb.r
  g = i.rgb.g
  b = i.rgb.b

  new_color = (r, g, b)
  colors_list.append(new_color)

t = Turtle()

t.speed("fastest")
t.hideturtle()
for j in range(-100, 150, 25):
  t.teleport(-100, j)
  for i in range(10):
    final_color = random.choice(colors_list)
    t.pencolor(final_color)
    t.penup()
    t.forward(25)
    t.pendown()
    t.fillcolor(final_color)
    t.begin_fill()
    t.circle(7)
    t.end_fill()
  












screen.exitonclick()