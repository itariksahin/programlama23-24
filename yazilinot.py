#iki yazılı notuna göre ortlama ve not hesaplayan program
yazili_1=int(input("Birinci yazılı notunu giriniz"))
yazili_2=int(input("ikinci yazılı notunu giriniz"))
ortalama=(yazili_1+yazili_2)/2
if ortalama<25 :
    print("0 aldınız")
elif ortalama<50:
    print("1 aldınız")
elif ortalama<60:
    print("2 aldınız")
elif ortalama<70:
    print("3 aldınız")
elif ortalama<85:
    print("4 aldınız")
else:
    print("5 aldınız")
print("------- Program bitti-------")
            
             
