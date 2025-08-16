def carpim():

    print("\n\nCARPIM TABLOSU\n")

    for aa in range(1, 11):
        print(f"\nBasamak: {aa}\n" + "----------------")
        for bb in range(1, 11):
            print(aa, "x", bb, "=", aa * bb)

    devam = input("Tabloyu tekrar yazdirmak ister misiniz? (e/h): ").lower()
    if devam != "e":
        print("Islem bitti. Simdi ana menuye yonlendiriliyorsunuz.")
        import proje_ana_ekrani
        proje_ana_ekrani.anamenu()

carpim()