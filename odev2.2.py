def hesap_makinesi(sayi1, sayi2, islem):

    if islem == '+':
        print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif islem == '-':
        print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif islem == '*':
        print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif islem == '/':
        if sayi2 == 0:
            print("Bolme islemi icin ikinci sayi 0 olamaz!")
        else:
            print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    else:
        print("Gecersiz islem turu!")

sayi1 = float(input("Birinci sayiyi girin: "))
sayi2 = float(input("İkinci sayiyi girin: "))
islem = input("Yapmak istediginiz islemi girin (+, -, *, /): ")

hesap_makinesi(sayi1, sayi2, islem)
