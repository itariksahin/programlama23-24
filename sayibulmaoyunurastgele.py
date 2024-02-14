#programda saklı bir sayı tahmin etme oyunudur.
import random
print("0 ile 1000 Arasında bir sayıyı tahmin etmeniz isteniyor")
sakli_sayi=random.randint(0,1000)
durum="h"
while (durum=="h"):
    tahmin=int(input("tahminizi giriniz"))
    if(tahmin>sakli_sayi):
        print("Büyük sayı girdiniz azaltın")
    elif (tahmin<sakli_sayi):
        print("Küçük sayı girdiniz artdırın")
    else:
        print("Doğru tahmin tebrikler")
        durum="e"
print("oyun bitti")
        
