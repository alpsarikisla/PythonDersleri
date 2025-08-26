notsayi = int(input("Kaç adet not gireceksiniz = "))

sayac = 0
toplam = 0

while sayac < notsayi:
    toplam += int(input("Lütfen " + str(sayac + 1) + ". Notu Giriniz = "))
    sayac += 1

ortalama = toplam / notsayi
print("Not Ortalamanız = " + str(ortalama))
