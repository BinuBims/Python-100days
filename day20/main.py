from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0,0),(-20,0),(-40,0)]

new_seg = []

for position in starting_positions:
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(position)
    new_seg.append(tim)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in new_seg:
        seg.forward(20)
screen.exitonclick()