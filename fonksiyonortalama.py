#2 yazılı 2 performans notunu dışarıdan alarak ortalama
#degeri geri döndüren programı fonksiyonm ile yazınız

#fonksiyon tanımlaması 
def not_hesapla(yazi1,yazili2,per1,per2):
    ortalama=(yazi1+yazili2+per1+per2)/4
    return ortalama

#ana program
not1=int(input("Birinci yazılı notunu giriniz"))
not2=int(input("İkinci yazılı notunu giriniz"))
not3=int(input("Birinci performans notunu giriniz"))
not4=int(input("İkinci performans notunu giriniz"))
hesapla=not_hesapla(not1,not2,not3,not4)
print("Ortalamanız=",hesapla)
