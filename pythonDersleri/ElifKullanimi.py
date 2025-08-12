# Not Ortalamasından başarı hesaplama
# 0 - 25    = 0
# 25 - 45   = 1
# 45 - 55   = 2
# 55 - 70   = 3
# 70 - 85   = 4
# 85 - 100  = 5

sinav1 = int(input("1. sınav notu = "))
sinav2 = int(input("2. sınav notu = "))

ortalama = (sinav1 + sinav2) / 2

print("Ortalamanız = " + str(ortalama))

if (ortalama >= 0) and (ortalama < 25):
    print("Notunuz 0")
elif (ortalama >= 25) and (ortalama < 45):
    print("Notunuz 1")
elif (ortalama >= 45) and (ortalama < 55):
    print("Notunuz 2")
elif (ortalama >= 55) and (ortalama < 70):
    print("Notunuz 3")
elif (ortalama >= 70) and (ortalama < 85):
    print("Notunuz 4")
elif (ortalama >= 85) and (ortalama <= 100):
    print("Notunuz 5")
else:
    print("Hatalı not girildi")
