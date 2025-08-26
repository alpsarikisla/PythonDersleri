# Kullanıcının girdiği verileri diziye dolduralım

sayi = int(input("Kaç adet ürün kaydedeceksiniz = "))

urunler = []

for x in range(sayi):
    urunler.append(input("Ürün Adı = "))

for urun in urunler:
    print(urun)
