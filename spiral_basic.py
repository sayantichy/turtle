import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

colors = ["red", "blue", "green", "yellow", "purple", "cyan", "white"]

for i in range(36):
    t.color(random.choice(colors))
    t.circle(100)
    t.right(10)

turtle.done()
