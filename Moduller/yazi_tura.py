def yt():

    import random
    import time

    print("\nYAZI-TURA OYUNU\n")

    while True:
        secim = input("Yazi mi tura mi? (y/t): ").lower()
        if secim not in ["y", "t"]:
            print("Lütfen sadece 'y' (yazi) veya 't' (tura) girin.")
            continue
        else:
            print ("Simdi kim kazanmis ogrenelim..")
            time.sleep(1)

        sonuc = random.choice(["y", "t"])
        if secim == sonuc:
            print("Tebrikler! Bildiniz.")
        else:
            print("Maalesef bilemediniz.")

        devam = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
        if devam != "e":
            print("Oyun bitti. Simdi oyunlar menusune yonlendiriliyorsunuz.")
            import proje_oyunlar_menusu

yt()