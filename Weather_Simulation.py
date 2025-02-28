import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Weather Simulation")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Raindrops list
raindrops = []

# Create raindrops
for _ in range(50):
    drop = turtle.Turtle()
    drop.speed(0)
    drop.shape("square")
    drop.color("blue")
    drop.shapesize(stretch_wid=0.2, stretch_len=0.2)
    drop.penup()
    drop.goto(random.randint(-400, 400), random.randint(100, 300))
    raindrops.append(drop)

# Snowflakes list
snowflakes = []

for _ in range(20):
    flake = turtle.Turtle()
    flake.speed(0)
    flake.shape("circle")
    flake.color("white")
    flake.shapesize(stretch_wid=0.3, stretch_len=0.3)
    flake.penup()
    flake.goto(random.randint(-400, 400), random.randint(100, 300))
    snowflakes.append(flake)

# Lightning
lightning = turtle.Turtle()
lightning.hideturtle()

# Update weather

def update_weather():
    screen.update()
    
    # Move raindrops
    for drop in raindrops:
        drop.sety(drop.ycor() - random.randint(5, 15))
        if drop.ycor() < -300:
            drop.goto(random.randint(-400, 400), random.randint(100, 300))
    
    # Move snowflakes
    for flake in snowflakes:
        flake.sety(flake.ycor() - random.randint(1, 5))
        if flake.ycor() < -300:
            flake.goto(random.randint(-400, 400), random.randint(100, 300))
    
    # Random lightning effect
    if random.randint(1, 100) > 98:
        screen.bgcolor("white")
        time.sleep(0.1)
        screen.bgcolor("black")
    
    screen.ontimer(update_weather, 50)

update_weather()
screen.mainloop()
