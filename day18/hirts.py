import colorgram
import turtle
from turtle import Screen 
import random
turtle.colormode(255)

tim = turtle.Turtle()
# colors = colorgram.extract("hirts..jpg", 30)
# color_pallet = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_pallet.append((r,g,b))
# print(color_pallet)

color_list = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), 
(39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), 
(199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), 
(224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), 
(81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]  
y = 0
for _ in range(10):
    tim.sety(y)
    tim.setx(0)
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.width(5)
        tim.dot()
        tim.penup()
        tim.forward(50)
    y += 50
    

screen = Screen()
screen.exitonclick()