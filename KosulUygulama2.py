# Kullanıcıdan isim ve DOĞUM YILI bilgisi alınacak
# YAŞ 10'dan büyük ise "sayın ..... yaş değeriniz uygundur"
# değil ise "Sayın ..... yaş değeriniz uygun değildir
isim = input("Lütfen adınızı giriniz = ")
dogumYilStr = input("Lütfen Doğum yılınızı giriniz = ")
dogumYil = int(dogumYilStr)
yas = 2025 - dogumYil
if yas >= 10:
    print("Sayın " + isim + " yaş değeriniz uygundur")
else:
    print("Sayın " + isim + " yaş değeri uygun değildir")
