def asal_mi(sayi):
    if sayi < 2:
        print(f" {sayi} bir asal sayı degildir.")
        return
    bolen = 2
    while bolen * bolen <= sayi:
        if sayi % bolen == 0:
            print(f"{sayi} bir asal sayi degildir. ({sayi}, {bolen} ile tam bolunebilir.)")
            return
        bolen += 1
    print(f"{sayi} bir asal sayidir. (Sadece 1 ve {sayi} ile bolunebilir.)")
sayi = int(input("Bir sayi girin: "))
asal_mi(sayi)
