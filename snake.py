import random
import turtle
import time

delay = 0.1
# Score
score = 0
high_score = 0


# Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")

# Set up the screen boundaries
window.setup(width=600, height=600)
window.tracer(0)  # Turns off the screen

# Snake head
head = turtle.Turtle()
head.shape('square')
head.color('red')
head.penup()
head.goto(0, 0)
head.direction = 'Stop'

# Snake food
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'blue'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0 High score: 0", align='center', font=('Monospace', 24, 'normal'))