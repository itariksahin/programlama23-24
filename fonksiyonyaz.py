#Fonksiyon ile ekrana belirli sayıda adınız yazan program
def yaz():
    sayac=int(input("Bir sayı giriniz"))
    ad=input("Adınız nedir")
    for i in range(1,sayac+1):
        print(ad)
yaz()
