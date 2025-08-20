# Turtle Kütüphanesi ile modül import etmek
import turtle
# turtle kütüphanesi projemize eklendi. artık kullanabiliriz

# turtle'ın oluşaçağı ekran
ekran = turtle.Screen()

# kaplumbağamızı oluşturduk
tospaa = turtle.Turtle()
tospaa.shape('turtle')
tospaa.pensize(5)

tospaa.forward(100)# 100 pixel ileri git
tospaa.left(90) #90 derece sola dön

tospaa.color('red')
tospaa.forward(100)
tospaa.left(90)

tospaa.color('blue')
tospaa.forward(100)
tospaa.left(90)

tospaa.color('green')
tospaa.forward(100)
tospaa.right(90)

turtle.done()