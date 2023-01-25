def kahve_yap(jeton):
    kahve_secenekleri = ["Espresso","Latte","Cappuccino"]
    bardak_boyutu = ["Küçük", "Orta", "Büyük"]
    if jeton == 1:
        print("jeton kabul edildi.")
        for i in range(len(kahve_secenekleri)):
            print(i+1, kahve_secenekleri[i])
        kahve_secimi = int(input("*********************\n"
                                 "Lütfen kahve seçiniz: "))
        for i in range(len(bardak_boyutu)):
            print(i+1, bardak_boyutu[i])
        bardak_secimi = int(input("*********************\n"
                                 "Lütfen bardak boyutu seçiniz: "))
        print(kahve_secenekleri[kahve_secimi-1], bardak_boyutu[bardak_secimi-1], "hazırlanıyor.")
    else:
        print("jeton kabul edilmedi.")

while True:
    jeton = int(input("jeton atınız: "))
    kahve_yap(jeton)