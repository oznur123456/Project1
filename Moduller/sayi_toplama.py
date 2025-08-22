def sayilar():

    import random

    print("\n\nMATEMATİK TOPLAMA ALIŞTIRMALARI\n")

    while True:
        seviye = int(input("Zorluk seviyesi ne olsun? (1/2/3): "))
        if 1 <= seviye <= 3:
            print(f"{seviye}. seviye seçtiniz...")
            break
        else:
            print("Lutfen gecerli bir sayi giriniz (1/2/3).")

    puan = 0
    olumlu = ["e", "evet", "evt", "olur", "devam", "ok", "x", " ", "okay", "tabi", "tabi ki"]
    devam = "e"

    while devam.lower() in olumlu:
        s1 = random.randint(1, 10 ** seviye)
        s2 = random.randint(1, 10 ** seviye)

        if int(input(f"{s1} + {s2} = ")) == s1 + s2:
            puan += 10
            print(f"Bildin, puanin {puan}.")
        else:
            puan -= 10
            print(f"Bilemedin, puanin {puan}.")

        devam = input("Devam etmek istiyor musun? ")
        if devam.lower() not in olumlu:
            print("Oyun bitti. Oyunlar menüsüne yönlendiriliyorsunuz...")
            import proje_oyunlar_menusu
            proje_oyunlar_menusu.oyun_menu()
            break

sayilar()

