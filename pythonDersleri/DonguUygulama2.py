# 0 - 100 arasındaki çift sayıları yazdırınız
sayi = 0
while sayi <= 100:
    print(sayi)
    sayi += 2

# konsoldan alınan sayıdan başlayarak 100 e kadar olan çift sayıları yazınız
sayi1 = int(input("Lütfen başlangıç değeri giriniz"))

while sayi1 <= 100:
    kalan = sayi1 % 2
    if kalan == 0:
        print(sayi1)
    sayi1 += 1

