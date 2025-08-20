# ÖDEV 1
# Konsoldan alınan ismi 15 kere merhaba "isim" şeklinde yazdırınız
isim = input("Lütfen isim giriniz = ")
for sayi in range(15):
    print(str(sayi + 1) + " - " + isim)

# ÖDEV 2
# konsoldan alınan 3 notun ortalamasını hesaplayın
# ortalama 50 den büyük ise geçti değilse kaldı yazın
print("Not hesaplayıcıya hoş geldiniz")

toplam = 0

for sayac in range(3):
    sinavNotu = input(str(sayac + 1) + ". sınav notunu giriniz = ")
    toplam += int(sinavNotu)

ortalama = toplam / 3
print("Ortalamanız = " + str(ortalama))
if ortalama >= 50:
    print("Geçtiniz...")
else:
    print("Kaldınız...")

# ÖDEV 3
# Karenin çevresini hesaplayan programı yazınız
kenar = int(input("Karenin 1 kenar uzunluğunu giriniz = "))
cevre = kenar * 4
print("Karenin çevresi = " + str(cevre))

