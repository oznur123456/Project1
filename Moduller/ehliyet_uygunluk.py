
def ehliyet():
    print("EHLIYET UYGUNLUK")
    yas = int (input ("Yasinizi giriniz:"))
    saglik_raporu = input("Saglik raporunuz var mi? (Evet/Hayir): ").lower()
    if yas >= 18 and saglik_raporu == "evet":
        print ("Ehliyet alabilirsiniz.")
    else:
        print ("Ehliyet alamazsiniz.")
    yas = int (input ("Yasinizi giriniz:"))
    saglik_raporu = input("Saglik raporunuz var mi? (Evet/Hayir): ").lower()
    if yas >= 18 and saglik_raporu == "evet":
        print("Ehliyet alabilirsiniz.")
    else:
        print("Ehliyet alamazsiniz.")

ehliyet()