import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Background color
screen.title("Interactive Spiral Effect with Multiple Turtles")

# Create the turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

# Setup turtle properties
def setup_turtle(t, color):
    t.shape("turtle")
    t.speed(0)
    t.width(2)
    t.color(color)
    t.penup()
    t.setpos(0, 0)
    t.pendown()

# Function to smoothly transition colors
def smooth_transition(t, colors):
    color_index = 0
    for i in range(100):
        t.color(colors[color_index % len(colors)])
        color_index += 1
        yield  # Move control back to the main loop

# Function for drawing starbursts and multiple spirals
def starburst_and_spirals(t, radius_start, angle_change, num_spirals=5):
    radius = radius_start
    for _ in range(num_spirals):
        for i in range(100):
            t.circle(radius)
            t.right(angle_change)
            radius += 2
            if i % 10 == 0:
                next(smooth_transition(t, ["red", "yellow", "blue", "purple", "cyan"]))
        radius_start += 10  # Increase initial radius for next spiral

# Function to handle multiple turtles drawing
def draw_multiple_turtles():
    setup_turtle(t1, "red")
    setup_turtle(t2, "blue")
    setup_turtle(t3, "green")

    t1.right(90)
    t2.left(45)
    t3.right(45)

    # Draw with multiple turtles
    for _ in range(5):
        starburst_and_spirals(t1, 10, 10)
        starburst_and_spirals(t2, 20, 20)
        starburst_and_spirals(t3, 30, 30)

# Function for interactive input
def change_colors_on_keypress():
    screen.onkey(lambda: t1.color("orange"), "1")
    screen.onkey(lambda: t2.color("pink"), "2")
    screen.onkey(lambda: t3.color("yellow"), "3")
    screen.listen()

# Function to change the background color dynamically
def dynamic_background():
    colors = ["black", "gray", "darkblue", "purple", "black"]
    while True:
        for color in colors:
            screen.bgcolor(color)
            turtle.delay(200)  # Delay to transition smoothly

# Function for glowing effect (using tracer)
def glow_effect():
    turtle.tracer(5, 0)  # Make drawing faster and smoother (glowing effect)
    turtle.update()

# Main function to combine everything
def main():
    draw_multiple_turtles()  # Draw spirals with multiple turtles
    change_colors_on_keypress()  # Change turtle colors interactively
    glow_effect()  # Enable glowing effect
    dynamic_background()  # Gradually change background color

    turtle.done()  # Finish drawing

# Run the main function
main()
