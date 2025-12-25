import turtle

# Setup the screen
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(25)
t.color("pink")
t.begin_fill()

# Draw the heart shape
t.left(140)
t.forward(113)

# Draw the left curve
for _ in range(200):
    t.right(1)
    t.forward(1)

t.left(120)

# Draw the right curve
for _ in range(200):
    t.right(1)
    t.forward(1)

t.forward(112)
t.end_fill()

# Hide turtle and keep window open
t.hideturtle()
turtle.done()