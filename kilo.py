#kilo programı
#30 kilo altı çılız
#30 ile 50 arası zayıf
#50 ile 60 arası normal
#60 ile 70 arası hafif kilolu
#70 ile 90 arası kilolu
#90 ile 110 arası şişman
#110 ile 130 arası obez
#130 dan büyükse eslem
kilo=int(input("Kilonuzu giriniz"))
if kilo<30:
    print("Çılız")
elif kilo<50:
    print("zayıf")
elif kilo<60:
    print("normal")
elif kilo<70:
    print("hafif kilolu")
elif kilo<90:
    print("kilolu")
elif kilo<110:
    print("şişman")
elif kilo<130:
    print("obez")
else:
    print("Eslem!!!!!")
print("Program bitti")    
