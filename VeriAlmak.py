# Veri Almak
# Yazdırmak için print() komutunun kullanıldığını biliyoruz
# konsoldan veri almak için input() komutu kullanılır
print("Lütfen adınızı giriniz")
# input komutu ile girilen veriyi isim değişkeni içerisine ata
isim = input()
# print("Merhaba " + isim)

soyisim = input("Lütfen soyadınızı giriniz = ")
print("Merhaba " + isim + " " + soyisim)

# input ile alınan her verinin türü string(metinseldir)
dogumYilstr = input("Lütfen Doğum yılınızı giriniz")
dogumYil = int(dogumYilstr)
yas = 2025 - dogumYil
print("Yaşınız = ")
print(yas)


