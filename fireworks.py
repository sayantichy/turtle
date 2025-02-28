import turtle
import random
import math

def draw_firework(x, y):
    firework = turtle.Turtle()
    firework.speed(0)
    firework.hideturtle()
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]
    
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    
    for _ in range(36):
        firework.color(random.choice(colors))
        firework.forward(50)
        firework.backward(50)
        firework.right(10)

def fireworks_show():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    for _ in range(10):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        draw_firework(x, y)
    
    screen.mainloop()

fireworks_show()
