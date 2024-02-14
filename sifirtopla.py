#Girilen sayı 0  olana kadar girilen tüm sayıları toplayan program
topla=0
girilen_Sayi=1
while(girilen_Sayi!=0):
    girilen_Sayi=int(input("Bir sayı giriniz"))
    topla=topla+girilen_Sayi
print("sonuç=",topla)
