# Turtle Up Down
import turtle

ekran = turtle.Screen()
imlec = turtle.Turtle()

imlec.fillcolor("red")
imlec.up()
imlec.backward(50)
imlec.down()
imlec.begin_fill()
imlec.forward(100)
imlec.left(120)
imlec.forward(100)
imlec.left(120)
imlec.forward(100)
imlec.left(120)
imlec.end_fill()

turtle.done()
