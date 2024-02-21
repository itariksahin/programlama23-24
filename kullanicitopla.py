#0 100000 arasındaRastgele sayı üreten ve bu sayıları kullanıcı isterse toplayab programa
import random
toplam=0
dongu=1
while dongu==1:
    sayi=random.randint(0,100000)
    print("üretilen sayı=",sayi)
    secim=input("Üretilen sayı toplama eklensin mi? evet=e hayır=h")
    if secim=="h":
        continue
    toplam=toplam+sayi
    secim2=input("Devam edilsin mi? evet=e hayır=h")
    if(secim2=="h"):
        break
print("Toplam=",toplam)
print("program bitti")
    
