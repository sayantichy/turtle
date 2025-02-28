import turtle
import random

def draw_spiral():
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    spiral = turtle.Turtle()
    spiral.speed(0)
    spiral.pensize(2)
    
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]
    
    for i in range(150):
        spiral.color(random.choice(colors))
        spiral.forward(i * 2)
        spiral.right(59)
        spiral.forward(i / 2)
        spiral.right(60)
    
    spiral.hideturtle()
    screen.mainloop()

draw_spiral()
