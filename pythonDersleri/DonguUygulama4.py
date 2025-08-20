# Konsoldan alınan 5 adet sayının ortalamasını yazdırınız
toplam = 0

for sayac in range(5):
    sayi = int(input("Lütfen sayı giriniz = "))
    toplam += sayi

ortalama = toplam / 5
print("Girilen sayıların ortalaması = " + str(ortalama))
