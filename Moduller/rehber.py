def rehber_menu():
    print("\033[1;33;40m")
    print("╔═════════════════════╗")
    print("║\033[1;35;40m     REHBER MENU   \033[1;33;40m  ║")
    print("║                     ║")
    print("║  1-Kisi ekle        ║")
    print("║  2-Kisi ara         ║")
    print("║  3-Rehberi listele  ║")
    print("║  4-Ana menu         ║")
    print("╚═════════════════════╝")
    print("\033[0m")

def rehber_ekle(rehber, isim, numara):
    rehber[isim.lower()] = numara
    print(f"{isim} rehbere eklendi.")

def rehber_ara(rehber, isim):
    return rehber.get(isim.lower(), "Bulunamadi.")

def rehber_listele(rehber):
    if rehber:
        print("\nRehber Listesi:")
        for isim, numara in rehber.items():
            print(f"{isim.capitalize()}: {numara}")
    else:
        print("Rehber bos.")

rehber = {}

while True:
    rehber_menu()
    secim = input("\nSeciminizi giriniz (1-4): ")

    if secim == "1":
        isim = input("Isim giriniz: ")
        numara = input(f"{isim} icin numara giriniz: ")
        rehber_ekle(rehber, isim, numara)

    elif secim == "2":
        isim = input("Aramak istediginiz isim: ")
        sonuc = rehber_ara(rehber, isim)
        print(f"Sonuc: {sonuc}")

    elif secim == "3":
        rehber_listele(rehber)

    elif secim == "4":
        print("Rehber uygulamasindan cikiyorsunuz. Simdi ana menuye yonlendiriliyorsunuz.")
        import proje_ana_ekrani
        
    else:
        print("Gecersiz secim, tekrar deneyin.")

    input("\nMenüye dönmek için Enter'a basın...")

rehber_menu()