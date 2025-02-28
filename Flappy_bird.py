import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Flappy Bird Clone")
screen.bgcolor("skyblue")
screen.setup(width=500, height=600)
screen.tracer(0)

# Bird setup
bird = turtle.Turtle()
bird.shape("circle")
bird.color("yellow")
bird.penup()
bird.goto(-100, 0)
bird.dy = 0

def jump():
    bird.dy = 8  # Jump power
    
screen.listen()
screen.onkeypress(jump, "space")

# Pipe setup
pipes = []

def create_pipes():
    top_pipe = turtle.Turtle()
    top_pipe.shape("square")
    top_pipe.color("green")
    top_pipe.shapesize(stretch_wid=15, stretch_len=3)
    top_pipe.penup()
    top_pipe.goto(200, random.randint(100, 250))
    
    bottom_pipe = turtle.Turtle()
    bottom_pipe.shape("square")
    bottom_pipe.color("green")
    bottom_pipe.shapesize(stretch_wid=15, stretch_len=3)
    bottom_pipe.penup()
    bottom_pipe.goto(200, top_pipe.ycor() - 250)
    
    pipes.append((top_pipe, bottom_pipe))

# Game loop
game_over = False

def update():
    global game_over
    screen.update()
    
    bird.dy -= 0.5  # Gravity effect
    bird.sety(bird.ycor() + bird.dy)
    
    if bird.ycor() < -280:
        game_over = True
    
    for top_pipe, bottom_pipe in pipes:
        top_pipe.setx(top_pipe.xcor() - 3)
        bottom_pipe.setx(bottom_pipe.xcor() - 3)
        
        if top_pipe.xcor() < -250:
            top_pipe.goto(200, random.randint(100, 250))
            bottom_pipe.goto(200, top_pipe.ycor() - 250)
        
        if bird.distance(top_pipe) < 20 or bird.distance(bottom_pipe) < 20:
            game_over = True
    
    if not game_over:
        screen.ontimer(update, 20)
    else:
        print("Game Over!")

# Ensure the bird movement is updated continuously
def game_loop():
    bird.sety(bird.ycor() + bird.dy)
    screen.ontimer(game_loop, 20)

create_pipes()
update()
game_loop()
screen.mainloop()
