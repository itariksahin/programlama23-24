#Program polis alma kuralı kontrol eder
#Bayan adaylar için boy 160 ve üzeri olmalıdır
#Erkek adaylar için boy 170 ve üzeri olmalıdır
boy=int(input("boyunuzu giriniz"))
cinsiyet=input("Cinsiyetinizi giriniz erkek=e bayan=b")
if cinsiyet!="e" and cinsiyet!="b":
    print("Yanlış secim yaptınız")
if cinsiyet=="b"and boy>160:
        print("Polis olabilir")
else:
    if cinsiyet=="e"and boy>170:
        print("Polis olabilir")
    else:
        print("Polis olamaz")
print("Program bitti")
