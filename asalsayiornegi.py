def asalmi(sayi):
    if (sayi == 1):
        return True
    elif (sayi == 2):
        return False
    else:
        for i in range(2, sayi):
            if (sayi % i == 0):
                return False
        return True

while True:
    sayi = input("lütfen sayı giriniz:")
    if (sayi == "q"):
        break
    sayi = int(sayi)
    if asalmi(sayi):
        print("bu asal bir sayıdır")
    else:
        print("bu asal bir sayı değildir")