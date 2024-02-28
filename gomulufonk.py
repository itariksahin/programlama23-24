# Fonksiyonlar belirli bir işi gerçekleştiren kod parçalarıdır
#Gömülü fonksiyonlar genelde kullanılan işlemler için hazırdır.
#Gömülü fonksiyonları kullanmak için kütüphane yüklemek gerekebilir.

import math

# karakök alan gömülü fonsiyon sqrt
kare=int(input("Karekökü alınacak sayıyı giriniz"))
print("Sayının karekökü=",math.sqrt(kare))

# girilen iki sayıda kuvvat alma işi yapar pow
taban_degeri=int(input("Bir sayı giiriniz"))
ust_deger=int(input("Kuvvet degerini giriniz"))
print(taban_degeri,"'nin ",ust_deger,"İçin kuvveti=",math.pow(taban_degeri,ust_deger))

#Girilen degeri tam sayıya yuvarlama ceil
sayi1=float(input("Kesirli sayı giriniz"))
print("Sayının yuvarlaması=",math.ceil(sayi1))

#mutlak deger alan fonksiyonumuz fabs
sayi2=float(input("Mutlak değerinin alınmasını istediğiniz sayıyı giriniz"))
print("Mutlak deger=",math.fabs(sayi2))
