from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun= snake.up, key="Up")
screen.onkey(fun= snake.down,key="Down")
screen.onkey(fun= snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

screen.exitonclick()
