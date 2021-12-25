from turtle import Screen, Turtle
import caterpillar as cater
from caterpillar import Caterpillar

ALIGNMENT = "left"
FONT = ("Didot", 24, "normal")

# define constant:
SCREEN_COLOR = (104,136, 89)

# # # setup screen # # #
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor(SCREEN_COLOR)
screen.title("The Beauty of Caterpillar's Movement")
screen.tracer(0)
a_caterpillar = Caterpillar()
screen.update()

# # # setup writer # # #
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")
writer.goto(-250, -50)




COUNT = 1
while True:
    a_caterpillar.move(screen)
    if COUNT == 1:
        writer.write("Nature optimizes itself.", align=ALIGNMENT, font=FONT)
    if COUNT == 3:
        writer.goto(-250, -100)
        writer.write("Just like mathematics behind this caterpillar.", align=ALIGNMENT, font=FONT)
    if COUNT == 5:
        writer.goto(-250, -150)
        writer.write("He takes the least action.", align=ALIGNMENT, font=FONT)
    if COUNT == 7:
        writer.goto(-250, -200)
        writer.write(";-)", align=ALIGNMENT, font=FONT)
    COUNT = COUNT + 1
    

    

screen.exitonclick()



