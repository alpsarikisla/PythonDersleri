# Kaç kişi kayıt edeceksiniz diye sorulacak
# kişilerin isimleri ve doğum yılları alınacak
# yaş 10 dan büyük ise diziye isim kaydedilecek
# kişi sayısı bittiğinde tüm dizi elemanları yazdırılacak

kisiSayi = int(input("Kaç kişi kayıt edilecek"))
kisiler = []

for x in range(kisiSayi):
    isim = input(str(x+1) + ". kişi adını giriniz =")
    dogumYili = int(input(str(x+1) + ". kişi doğum yılı = "))
    yas = 2025 - dogumYili
    if yas >= 10:
        kisiler.append(isim)

print("Yaşı tutan kayıtlı kişi sayısı = " + str(len(kisiler)))
print("*-*-*- Kişiler -*-*-*")
for kisi in kisiler:
    print(kisi)
