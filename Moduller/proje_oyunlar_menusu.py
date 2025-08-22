
def oyun_menu():
    print("\033[1;33;40m")
    print("╔═════════════════════╗")
    print("║\033[1;35;40m    OYUNLAR MENU   \033[1;33;40m  ║")
    print("║                     ║")
    print("║  1-Tas Kagit Makas  ║")
    print("║  2-Yazi Tura        ║")
    print("║  3-Sayi Toplama     ║")
    print("║  4-Sayi Tahmin      ║")
    print("║  5-Ana menüye dön   ║")
    print("║                     ║")
    print("║   Seçiminiz nedir?  ║")
    print("╚═════════════════════╝")
    print("\033[0m") 

    ss = int(input())

    if ss == 1 : 
        print("Tas kagit makas basliyor...")
        import tas_kagit_makas
        tas_kagit_makas.tkm()   

    if ss == 2 : 
        print("Yazi tura basliyor...")
        import yazi_tura
        yazi_tura.yt()

    if ss == 3 : 
        print("Sayi toplama basliyor...")
        import sayi_toplama
        sayi_toplama.sayilar()

    if ss == 4 : 
        print("Sayi tahmin oyunu basliyor...")
        import sayi_tahmin
        sayi_tahmin.tahmin()  

    if ss == 5 :
        import proje_ana_ekrani
        proje_ana_ekrani.anamenu()

oyun_menu()
    





