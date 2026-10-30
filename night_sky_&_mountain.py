import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("midnight blue")
screen.title("Night Sky and Mountains")

bob = turtle.Turtle()
bob.speed(0)
bob.pensize(2)
bob.shape("blank")

# Draw the moon
def draw_moon():
    bob.penup()
    bob.goto(150, 150)
    bob.color("yellow")
    bob.pendown()
    bob.begin_fill()
    bob.circle(40)
    bob.end_fill()

    # Cover part of the moon to create a crescent
    bob.penup()
    bob.goto(170, 165)
    bob.color("midnight blue")
    bob.pendown()
    bob.begin_fill()
    bob.circle(35)
    bob.end_fill()

# Draw evenly spaced stars in random positions
def draw_stars():
    bob.color("white")

    for i in range(20):
        x = -350 + (i % 5) * 140 + random.randint(-30, 30)
        y = 60 + (i // 5) * 65 + random.randint(-20, 20)
        size = random.randint(8, 15)

        bob.penup()
        bob.goto(x, y)
        bob.pendown()
        bob.begin_fill()

        for j in range(5):
            bob.forward(size)
            bob.right(144)

        bob.end_fill()

# Draw clouds
def draw_cloud(x, y):
    bob.color("light gray")

    for i in range(3):
        bob.penup()
        bob.goto(x + i * 25, y)
        bob.pendown()
        bob.begin_fill()
        bob.circle(20)
        bob.end_fill()

# Draw mountains
def draw_mountain(x, y, color):
    bob.penup()
    bob.goto(x, y)
    bob.color(color)
    bob.pendown()
    bob.begin_fill()

    bob.goto(x + 100, y + 180)
    bob.goto(x + 200, y)
    bob.goto(x, y)

    bob.end_fill()

# Draw snow on mountains
def draw_snow(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.color("white")
    bob.pendown()
    bob.begin_fill()

    bob.goto(x + 100, y + 180)
    bob.goto(x + 75, y + 135)
    bob.goto(x + 60, y + 150)
    bob.goto(x + 45, y + 125)
    bob.goto(x + 30, y + 140)
    bob.goto(x, y)

    bob.end_fill()

# Draw trees
def draw_tree(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.color("dark green")
    bob.pendown()
    bob.begin_fill()

    bob.goto(x + 20, y + 70)
    bob.goto(x + 40, y)
    bob.goto(x, y)

    bob.end_fill()

    # Draw tree trunk
    bob.penup()
    bob.goto(x + 15, y)
    bob.color("brown")
    bob.pendown()
    bob.begin_fill()

    for i in range(4):
        bob.forward(10)
        bob.left(90)

    bob.end_fill()

# Draw the ground
def draw_ground():
    bob.penup()
    bob.goto(-400, -150)
    bob.color("dark green")
    bob.pendown()
    bob.begin_fill()

    bob.goto(400, -150)
    bob.goto(400, -300)
    bob.goto(-400, -300)
    bob.goto(-400, -150)

    bob.end_fill()

# Call all functions
draw_moon()
draw_stars()

# Draw clouds
draw_cloud(-250, 130)
draw_cloud(-50, 230)
draw_cloud(220, 100)

# Draw mountains
draw_mountain(-300, -150, "slate blue")
draw_mountain(-100, -150, "dark slate blue")
draw_mountain(100, -150, "slate blue")

# Draw snow
draw_snow(-300, -150)
draw_snow(-100, -150)
draw_snow(100, -150)

# Draw ground
draw_ground()

# Draw 4 trees using a loop
for i in range(4):
    draw_tree(-280 + i * 180, -150)

bob.hideturtle()

turtle.done()
