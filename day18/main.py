from turtle import Turtle, Screen
import turtle as t
import random
#drawing a square
tim = Turtle()
# tim.shape("square")
# tim.color("red")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    col_tup = (r,g,b)
    return col_tup

# random_turn = [0,90,180,270]
# for _ in range(200):
#     tim.color(random_color())
#     tim.width(10)
#     tim.speed(0)
#     tim.forward(30)
#     tim.setheading(random.choice(random_turn))

#drawing a spirograph
for _ in range(360//10):
    tim.circle(100)
    tim.color(random_color())
    tim.width(2)
    tim.setheading(tim.heading() +10)
    tim.speed(0)

screen = Screen()
screen.exitonclick()