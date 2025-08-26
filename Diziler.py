# Diziler birden çok veriyi bir arada tutmak için kullanılan yapıdır
# Örneğin 5 adet araba markasını tutmak istediğimizde 5 adet değişken oluşturmak gerekir
# ancak bu 5 adet değişkeni yönetmek kolay değildir
# bu sebeple bu verileri bir arada belirli bir SıraNumarası(index) ile tutma aracına
# dizi(array) denir
araba1 = "Volvo"
araba2 = "BMW"
araba3 = "Fiat"
araba4 = "Ford"
araba5 = "Hyundai"

# üstteki kullanım yerine
arabalar = ["Volvo", "BMW", "Fiat", "Ford", "Hyundai"]
print(arabalar)

for oto in arabalar:
    print(oto)
