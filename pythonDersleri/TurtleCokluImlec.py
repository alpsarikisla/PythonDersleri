# Turtle Up Down
import turtle

ekran = turtle.Screen()

imlec1 = turtle.Turtle()
imlec1.color("Purple")

imlec2 = turtle.Turtle()
imlec2.color("Aqua")

imlec1.up()
imlec2.up()

imlec1.goto(-300, +50)
imlec2.goto(-300, -50)

imlec1.down()
imlec2.down()

imlec1.speed(1)
imlec2.speed(6)
imlec1.forward(600)
imlec2.forward(600)

turtle.done()
