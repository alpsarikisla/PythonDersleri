# Yan yana uzunlukları ve aralarındaki boşlukları
# 50 pixel olan Mavi Renkli Kesikli 9 Çizgi Çizimi

import turtle

ekran = turtle.Screen()
imlec = turtle.Turtle()
imlec.color("blue")

imlec.penup()
imlec.back(450)
imlec.pendown()

for sayac in range(9):
    imlec.forward(50)
    imlec.penup()
    imlec.forward(50)
    imlec.pendown()

turtle.done()
