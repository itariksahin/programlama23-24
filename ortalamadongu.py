#Kullanıcının istediği kadar sayının ortalamasını bulan program
ort_sayi=int(input("Kaç tane sayının ortalaması alınacak"))
topla=0
for sayac in range(ort_sayi):
    sayi=int(input("Bir sayı giriniz"))
    topla=topla+sayi
ortalama=topla/ort_sayi
print("sonuç=",ortalama)
