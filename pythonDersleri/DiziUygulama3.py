# Kaç adet çizgi çizeceksiniz diye sorulacak
# çizilecek her çizgi için renk adı alınacak
# renkler diziye atılıp
# çizgiler çizdirilecek
import turtle

cizgiSayi = int(input("Kaç Adet Çizgi Çizilecek = "))

renkler = []
for x in range(cizgiSayi):
    renk = input(str(x + 1) + ". rengi ingilizce yazınız = ")
    renkler.append(renk)

ekran = turtle.Screen()
imlec = turtle.Turtle()

imlec.penup()
imlec.back(400)
imlec.pendown()

for renk in renkler:
    imlec.color(renk)
    imlec.forward(50)
    imlec.penup()
    imlec.forward(30)
    imlec.pendown()

turtle.done()
