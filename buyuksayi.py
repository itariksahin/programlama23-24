#Kullanıcının girdiği 3 sayıdan büyük olanını ekrana yazdırınız.
sayi1=int(input("Sayı biri giriniz"))
sayi2=int(input("Sayı ikiyi giriniz"))
sayi3=int(input("Sayı üçü giriniz"))
if sayi1>sayi2 and sayi1>sayi3:
    print("Sayı 1 en büyük sayıdır")
elif sayi2>sayi1 and sayi2>sayi3:
    print("Sayı 2 en büyük sayıdır")
elif sayi3>sayi2 and sayi3>sayi1:
    print("Sayı 3 en büyük sayıdır")
else:
    print("eşitlik var")
