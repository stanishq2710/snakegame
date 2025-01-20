import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# used to turn off/on the animations
# when the tracer is turned off,you run the code just a black screen will appear
# we can use update method when the tracer is off to refresh or redraw the screen

snake = Snake()
food = Food()
scoreboard = Score()


screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detecting the collision from food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()
    # detecting collision with the wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() >280 or snake.segments[0].ycor() <-280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # detecting collision with tail
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) <10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()