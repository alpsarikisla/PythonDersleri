# Döngü mantığı ve kullanımı
# temelde aynı işi birden çok kez yapacağımız durumlarda döngü kullanırız
# Döngünü temel kuralı Bir başlangıç ve bir bitiş noktası belirlenmesidir

# 0 dan 5 e kadar olan sayıları yazdırınız
print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print("*-*-*--*-*-*-*")
# Döngü kullanımı (for döngüsü)
# sayi degiskeni içerisindeki veri 0 dan başlar Range ile belirtilen sınıra kadar gider
for sayi in range(10):
    print(sayi)

print("*-*-*--*-*-*-*")

# döngü kullanımı (While döngüsü)
# 10 dan başlayıp 20 ye kadar olan sayıları yazdırınız
sayi1 = 10

# bu şart sağlandığı sürece döngüye devam et
while sayi1 <= 20:
    print(sayi1)
    sayi1 += 1
print("Döngü tamamlandı")

