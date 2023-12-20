#Kullanıcıdan iki sayı alan kullanıcının seçtiği işleme göre dört işlemden
#birini yapıp sonucu ekrana yazan program.
sec=input("Bire işlem seciniz 1-topla 2-cıkarma 3-bölme 4-çarpma ")
sayi_1=int(input("birinci sayıyı giriniz"))
sayi_2=int(input("birinci sayıyı giriniz"))
if sec=="1":
    sonuc=sayi_1+sayi_2
elif sec=="2":
    sonuc=sayi_1-sayi_2
elif sec=="3":
    sonuc=sayi_1/sayi_2
elif sec=="4":
    sonuc=sayi_1*sayi_2
else:
    print("yanlış secim")
print("İşlem sonucu =",sonuc)
print("-----------")
