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
food.shape('square')
food.color('green')
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

# Function
def group():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
window.listen()
window.onkeypress(group, 'w')
window.onkeypress(go_down, 's')
window.onkeypress(go_left, 'a')
window.onkeypress(go_right, 'd')

segments = []

while True:
    window.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'Stop'
        colors = random.choice(['red', 'green', 'blue'])
        shapes = random.choice(['square', 'triangle', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('Monospace', 24, 'normal'))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('orange')
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('Monospace', 24, 'normal'))
    # Check for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            colors = random.choice(['red', 'green', 'blue'])
            shapes = random.choice(['square', 'triangle', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('Monospace', 24, 'normal'))
    time.sleep(delay)
window.mainloop()