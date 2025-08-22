
def ehliyet():
    print ("EHLIYET UYGUNLUK DURUMU")
    while True:
        yas = int(input("Yasinizi giriniz: "))
        saglik_raporu = input("Saglik raporunuz var mi? (Evet/Hayir): ").lower()

        if yas >= 18 and saglik_raporu == "evet":
            print("Ehliyet alabilirsiniz.")
        else:
            print("Ehliyet alamazsiniz.")

        devam = input("\nBaşka işlem yapmak ister misiniz? (e/h): ").lower()
        if devam != "e":
            print("Ana ekrana yönlendiriliyorsunuz...")
            import proje_ana_ekrani
            proje_ana_ekrani.anamenu()

ehliyet()
