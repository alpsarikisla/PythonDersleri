# kullanıcıdan 2 adet not alınacak notların ortalaması 50 üstü ise geçtiniz
# değilse kaldınız yazılacak
sayi1str = input("Lütfen 1. sınav notunuzu giriniz = ")
sayi1 = int(sayi1str)

sayi2str = input("Lütfen 2. sınav notunuzu giriniz = ")
sayi2 = int(sayi2str)

ortalama = (sayi1 + sayi2) / 2

print("Not ortalamanız = " + str(ortalama))

if ortalama >= 50:
    print("Geçtiniz")
else:
    print("Kaldınız")
