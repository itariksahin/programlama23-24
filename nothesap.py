#iki yazılı iki performans istenirse
#bir proje notuna göre geçme kalma hesaplayan programı yazınız

proje_tercih=input("Proje notu hesaplansın mı? e-evet h-hayır")
yazili1=int(input("1. Yazılı notunu giriniz"))
yazili2=int(input("2. Yazılı notunu giriniz"))
performans1=int(input("1. Performans notunu giriniz")) 
performans2=int(input("2. Performans notunu giriniz"))
if(proje_tercih=="e"):
    projenotu=int(input("proje notunu giriniz"))
    ortalama=(yazili1+yazili2+performans1+performans2+projenotu)/5
else:
    ortalama=(yazili1+yazili2+performans1+performans2)/4
if ortalama<25:
    print("Ortalama=",ortalama,"-0 notu ile kaldı")
elif ortalama<50:
    print("Ortalama=",ortalama,"-1 notu ile kaldı")
elif ortalama<65:
    print("Ortalama=",ortalama,"-2 notu ile geçti")
elif ortalama<70:
    print("Ortalama=",ortalama,"-3 notu ile geçti")
elif ortalama<85:
    print("Ortalama=",ortalama,"-4 notu ile geçti")
elif ortalama<101:
    print("Ortalama=",ortalama,"-5 notu ile geçti")
else:
    print("yanlış not hesapı böyle bir not ortalaması olamaz")
print("----------------------------")
