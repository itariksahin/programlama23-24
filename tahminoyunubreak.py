#tahmin oyunu(0 ile 10000 arası saklı sayıyı bulma)
import random
sakli_Sayi=random.randint(0,10000)
durum="e"
while durum=="e":
    tahmin=int(input("tahmininiz nedir?"))
    if tahmin>sakli_Sayi:
        print("Büyük sayı girdiniz küçültünüz")
    elif tahmin<sakli_Sayi:
        print("Küçük sayı girdiniz büyültün")
    else :
        print("tahminiz doğru tebrikler")
        break
print("Oyun bitti")
