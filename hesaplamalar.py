def hesapmenu():
    print("\033[1;33;40m")
    print("╔═════════════════════╗")
    print("║\033[1;35;40m   HESAP MAKINESI  \033[1;33;40m  ║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Cikarma          ║")
    print("║  3-Bolme            ║")
    print("║  4-Carpma           ║")
    print("║  5-Kare             ║")
    print("║  6- Ana menuye don  ║")
    print("║                     ║")
    print("║   Seçiminiz nedir?  ║")
    print("╚═════════════════════╝")
    print("\033[0m")  

    s = int(input("Seçiminiz?"))
    if s == 1: topla()
    elif s == 2: cikar()
    elif s == 3: bol()
    elif s == 4: carp()
    elif s == 5: kare()
    elif s == 6:
        import proje_ana_ekrani

def topla():
    a = int(input("Birinci sayi giriniz: "))
    b = int(input("Ikinci sayiyi giriniz: "))
    print("Toplam: ",a+b)
    hesapmenu()

def cikar():
    c = int(input("Birinci sayi giriniz: "))
    d = int(input("Ikinci sayiyi giriniz: "))
    print("Sonuc: ",c-d)
    hesapmenu()

def bol():
    e = int(input("Birinci sayi giriniz: "))
    f = int(input("Ikinci sayiyi giriniz: "))
    print("Sonuc: ",e/f)
    hesapmenu()

def carp():
    g = int(input("Birinci sayi giriniz: "))
    h = int(input("Ikinci sayiyi giriniz: "))
    print("Sonuc: ",g*h)
    hesapmenu()

def kare():
    i = int(input("Sayiyi giriniz: "))
    print("Sonuc: ",i**2)
    hesapmenu()


hesapmenu()


