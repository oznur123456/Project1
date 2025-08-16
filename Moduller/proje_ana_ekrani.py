def selamla(): print("Merhaba!")
def anamenu():
    print("\033[1;35;40m")
    print("╔═══════════════════════╗")
    print("║\033[1;33;40m     VEKTOREL APP    \033[1;35;40m  ║")
    print("║                       ║")
    print("║  1-Hesaplamalar       ║")
    print("║  2-Oyunlar            ║")
    print("║  3-Çizimler           ║")
    print("║  4-Takvim             ║")
    print("║  5-Ritmik Sayma       ║")
    print("║  6-Not Hesaplama      ║")
    print("║  7-Carpim Tablosu     ║")
    print("║  8-BMI Hesaplama      ║")
    print("║  9-Doviz Uygulamasi   ║")
    print("║ 10-Sicaklik Hesaplama ║")
    print("║ 11-Cikis              ║")
    print("║   Seçiminiz nedir?    ║")
    print("╚═══════════════════════╝")
    print("\033[0m") 
     
    secim = int(input())
    print("Seçiminiz:",secim,"idi.")

    if secim < 1 or secim > 11:
        print("Secim yanlis. 1-10 arasi bir deger giriniz.")
        anamenu()

    elif secim == 1:
        print("Hesaplamalari seçtiniz.")
        import hesaplamalar
        hesaplamalar.hesapmenu()
        
    elif secim == 2: 
        print("Oyunlar seçtiniz.")
        import proje_oyunlar_menusu
        proje_oyunlar_menusu.oyun_menu()
    
    elif secim == 3:
        print("Cizimleri seçtiniz.")
        import cizimler
        cizimler.cizim_menu()

    elif secim == 6:
        print("Not hesaplamayi seçtiniz.")
        import not_hesaplama
        not_hesaplama.notlar()
    
    elif secim == 7:
        print("Carpim tablosunu seçtiniz.")
        import carpim_tablosu
        carpim_tablosu.carpim()

    anamenu()

selamla()
anamenu()





