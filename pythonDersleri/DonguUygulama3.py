# Kullanıcıdan alınan 5 sayının toplamını yazdırınız
toplam = 0

for sayac in range(5):
    sayi = int(input("Lütfen sayı giriniz = "))
    toplam += sayi

print("Girilen sayıların toplamı = " + str(toplam))
