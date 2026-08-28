import turtle

# screen settings

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Rose 🌹")

# make a turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.hideturtle()

# making petal

def petal(size):
    t.begin_fill()

    for _ in range(2):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(120)

    t.end_fill()

# making a Rose flower

def draw_rose():
    t.color("darkred", "red")

    for _ in range(12):
        petal(70)
        t.left(30)

    t.color("darkred", "crimson")

    for _ in range(10):
        petal(50)
        t.left(30)

    t.color("darkred", "red")

    for _ in range(8):
        petal(30)
        t.left(45)


# making stem

def draw_stem():
    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()

    t.color("darkgreen")
    t.pensize(10)

    t.fd(250)


# making leaf

def draw_leaf(size=70):
    t.begin_fill()

    for _ in range(2):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(120)

    t.end_fill()


# making leaves

def draw_leaves():

    t.color("darkgreen", "green")
    t.pensize(2)

    # left leaf

    t.penup()
    t.goto(0, -180)
    t.setheading(150)
    t.pendown()

    draw_leaf(60)

    # right leaf

    t.penup()
    t.goto(0, -220)
    t.setheading(30)
    t.pendown()

    draw_leaf(60)


# start a program


#stem
draw_stem()

#leaves
draw_leaves()

# go to center
t.penup()
t.goto(0, -50)
t.setheading(0)
t.pendown()

# flower
draw_rose()


turtle.done()