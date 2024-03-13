#faktoriyel hesabı yapan fonksiyon
def faktoriyel(say):
    fak=1
    for i in range (1,say+1):
        fak=fak*i
    print("Faktoriyel sonucu=",fak)
sayi=int(input("FAktöriyeli hesaplanacak sayıyı giriniz"))
faktoriyel(sayi)
