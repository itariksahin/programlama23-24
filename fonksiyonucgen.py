#üçgen çizen fonksiyon
def yildiz_ucgen_ciz():
    say=int(input("Üçken için satır sayısını giriniz"))
    print("Yıldız üçgen çiziliyor:")
    for satir in range(1,say+1):
        print ("*" * satir)
yildiz_ucgen_ciz()
