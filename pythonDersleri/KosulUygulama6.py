# kullanıcıdan alınan sayı 0 - 100 aralığı dışında mı?
sayi = int(input("Lütfen sayı giriniz"))
if sayi < 0 or sayi > 100:
    print("Sayı aralık dışında")
else:
    print("Sayı aralıkta")
