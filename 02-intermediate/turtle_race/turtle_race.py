import turtle
import random

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink']


# Number of turtles

while True:

    try:
        number_of_turtles = int(
            input("How many turtles? ")
        )

        if 2 <= number_of_turtles <= 6:
            break

        print("Please enter a number between 2 and 6.")

    except ValueError:
        print("Invalid input. Please enter a number between 2 and 6.")


# User's guess

available_turtles = colors[:number_of_turtles]

print("Available turtles:", ", ".join(available_turtles))

while True:

    guess = input("Guess which color will win: ").strip().lower()

    if guess in available_turtles:
        break

    print("Please choose one of the available colors.")


# Screen

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(500, 500)
screen.title("Turtle Race")


# Create turtles

x_positions = [-200, -120, -40, 40, 120, 200]

turtles = []

for color, x in zip(available_turtles, x_positions):

    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.shapesize(1.5)
    t.setheading(90)

    t.penup()
    t.goto(x, -220)
    t.pendown()

    turtles.append(t)


# Race

finished = []

while len(finished) < len(turtles):

    for t in turtles:

        # Don't move turtles that already finished
        if t in finished:
            continue

        t.forward(random.randint(1, 10))

        # Turtle reached the finish line
        if t.ycor() >= 220:

            finished.append(t)

            # Stop when we have first 3 places
            if len(finished) == 3:
                break


# Results

print("\n===== RESULTS =====")

first = finished[0].pencolor()
second = finished[1].pencolor()
third = finished[2].pencolor()

print(f"🥇 1st place: {first}")
print(f"🥈 2nd place: {second}")
print(f"🥉 3rd place: {third}")


# Check guess

if guess == first:
    print("\nYou guessed correctly! 🎉")
else:
    print("\nYou guessed wrong! ❌")
    print(f"The winner was {first}.")


turtle.done()