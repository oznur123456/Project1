def notlar():
    print("\033[1;33;40m")
    print("╔═════════════════════════════════════╗")
    print("║\033[1;35;40m           NOT HESAPLAMA           \033[1;33;40m  ║")
    print("║                                     ║")
    print("║  1-Donem Sonu Notu                  ║")
    print("║  2-Harf Notu ve Gecme-kalma Durumu  ║")
    print("║  3-Ana menuye don                   ║")
    print("╚═════════════════════════════════════╝")
    s = int(input("Seçiminiz?"))
    if s == 1: donem_sonu()
    elif s == 2: puan() 
    elif s == 3:
            import proje_ana_ekrani


def donem_sonu():
    a = int(input("1. vize notunuzu giriniz: "))
    b = int(input("2. vize notunuzu giriniz: "))
    c = int(input("Final notunuzu giriniz: "))
    print("Toplam: ",a*3/10+b*3/10+c*4/10)
    notlar()

def puan ():
    puan = float(input ("Donem sonu notunuzu giriniz: "))
    if puan >= 90:
        print ("Harf notunuz: AA")
        print ("Tebrikler, dersten gectiniz!")
    elif puan >= 80:
        print ("Harf notunuz: BB")
        print ("Tebrikler, dersten gectiniz!")
    elif puan >= 70:
        print ("Harf notunuz: CC")
        print ("Tebrikler, dersten gectiniz!")
    elif puan >= 60:
        print ("Harf notunuz: DD")
        print ("Tebrikler, dersten gectiniz!")
    else:
        print ("Harf notunuz: F")
        print ("Dersten kaldiniz.")
    notlar()


if __name__ == '__main__': notlar()