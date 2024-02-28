import math
#Girilen sayının sin cos tan asin acos ve atan bulma (trigonometrik fonk)
Deger=int(input("Trigonometrik hesap için açı giriniz"))
print("Sinüsü=",math.sin(Deger))
print("kosinüsü=",math.cos(Deger))
print("Tanjantı=",math.tan(Deger))
print("Kotanjantı=",math.atan(Deger))
print("Arcsinüsü=",math.asin(math.sin(Deger)))
print("Arckosinüsü=",math.acos(math.cos(Deger)))
print("--------")
#10 tabanına göre logaritma hesaplama log10
sayi1=int(input("Logaritması hesaplanacak sayıyı giriniz"))
print("Logaritma=",math.log10(sayi1))
#Girilen taban degerine göre logaritma log
sayi2=int(input("Logaritması hesaplanacak sayıyı giriniz"))
taban=int(input("Logaritmanın taban degeriniz giriniz"))
print("Logaritma=",math.log(sayi2,taban))
#girilen sayının faktöriyeli factorial
fakt=int(input("FAktoriyeli hesaplanacak sayıyı giriniz"))
print("Kaktoriyel=",math.factorial(fakt))
