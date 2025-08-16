def tkm():
    import random
    print("\nTAS-KAGIT-MAKAS OYUNU\n")

    secenekler = ["tas", "kagit", "makas"]

    while True:
        secim = input("Taş, kagit veya makas? ").lower()
        if secim not in secenekler:
            print("Lütfen sadece taş, kagit veya makas yazin.")
            continue

        bilgisayar = random.choice(secenekler)
        print(f"Bilgisayar: {bilgisayar}")

        if secim == bilgisayar:
            print("Berabere!")
        elif (secim == "tas" and bilgisayar == "makas") or \
             (secim == "kagit" and bilgisayar == "tas") or \
             (secim == "makas" and bilgisayar == "kagit"):
            print("Kazandiniz!!")
        else:
            print("Kaybettiniz")

        devam = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
        if devam != "e":
            print("Oyun bitti. Simdi oyunlar menusune yonlendiriliyorsunuz.")
            import proje_oyunlar_menusu
tkm()
