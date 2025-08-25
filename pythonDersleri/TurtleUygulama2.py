# Yan yana uzunlukları ve aralarındaki boşlukları kullanıcıdan alınan
# Kullanıcıdan alınan sayı kadar çizgi oluşturun
import turtle
uzunluk = int(input("Çizgi uzunluğunu giriniz = "))
bosluk = int(input("Boşluk uzunluğunu giriniz = "))
adet = int(input("Çizgi adedini giriniz = "))
renk = input("Çizgi rengini ingilizce olarak yazınız = ")

ekran = turtle.Screen()
imlec = turtle.Turtle()
imlec.color(renk)

imlec.penup()
imlec.back(450)
imlec.down()

for x in range(adet):
    imlec.forward(uzunluk)
    imlec.penup()
    imlec.forward(bosluk)
    imlec.pendown()

print("Çiziminiz tamamlandı. ekranı kontrol ediniz")
turtle.done()
