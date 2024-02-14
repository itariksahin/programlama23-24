#Bu program faktöriyel hesaplamak içindir
sayac=1
faktoriyel=1
faktoriyel_degeri=int(input("faktöriyeli hesaplanacak sayıyı giriniz"))
while(sayac<=faktoriyel_degeri):
    faktoriyel=faktoriyel*sayac
    sayac=sayac+1
print("sonuç =",faktoriyel)
