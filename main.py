# Create a snake body

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.goto(position)

# Move the snake
# Control the snake
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail

screen.exitonclick()
