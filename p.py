<<<<<<< HEAD
print("This is file p.py")
print("Hello from p.py!")
print("End of p.py")
print("End of p")
print("Hi this is the newF")
<<<<<<< HEAD

def draw_tree(height):
    # Draw the leaves of the tree
    for i in range(height):
        # Calculate spaces to center the stars
        print(' ' * (height - i - 1) + '#' * (2 * i + 1))
    
    # Draw the trunk (centered)
    for t in range(2):
        print(' ' * (height - 1) + '||')

# Set how tall you want your tree to be
draw_tree(10)
draw_tree(3*2)
=======
print("this is the second change in p.py") 
print("Final change in p.py")

>>>>>>> f1534cb (the second commit in py)
=======
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
>>>>>>> 6762404 (add heart)
