#1000 kadar sayarken tek sayılarda adı çift sayılarda soyadı ekrana yazan prog.
Ad=input("Adınızı giriniz")
Soyad=input("Soyadınızı giriniz")
sayac=1
while(sayac<1001):
    if sayac%2==1:
        print(Ad)
    else:
        print(Soyad)
    sayac=sayac+1
print("Program sona erdi")
