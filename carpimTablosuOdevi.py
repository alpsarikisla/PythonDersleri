# ÖDEV 4
# Çarpım tablosunun 3 ler basamağını yazdırın
# 1 X 3 = 3
# 2 X 3 = 6 şeklinde yazılacak
for sayi in range(10):
    carpan = sayi + 1
    print("3 X " + str(carpan) + " = " + str(carpan * 3))

# konsoldan alınan basamak değerinin çarpım tablosunu yazınız

basamak = int(input("Lütfen tablosu yazdırılacak basamak değerini giriniz = "))

for sayi in range(10):
    carpan = sayi + 1
    print(str(basamak) + " X " + str(carpan) + " = " + str(basamak * carpan))