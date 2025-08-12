# Kullanıcıdan kullanıcı adı  ve şifre alınacak
# kullanıcı adı admin ve şifre 1234 ise hoş geldin admin
# değilse Kullanıcı bulunamadı yazılacak
print("*-*-*-*- HOŞGELDİNİZ -*-*-*-*")
print("Giriş yapmak için lütfen kullanıcı adı ve şifre giriniz")
kullaniciAdi = input("Kullanıcı Adınız = ")
sifre = input("Şifreniz = ")

if kullaniciAdi == "n.sarikisla" and sifre == "1234":
    print("Hoşgeldin Nilgün")
else:
    print("Giriş Başarısız")
    print("Kullanıcı bilgileri hatalı")
