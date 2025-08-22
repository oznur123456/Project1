def selamla(): print("Merhaba!")
def anamenu():
    print("\033[1;35;40m")
    print("╔═══════════════════════╗")
    print("║\033[1;33;40m     VEKTOREL APP    \033[1;35;40m  ║")
    print("║                       ║")
    print("║  1-Hesaplamalar       ║")
    print("║  2-Oyunlar            ║")
    print("║  3-Çizimler           ║")
    print("║  4-Rehber             ║")
    print("║  5-Ehliyet Uygunluk   ║")
    print("║  6-Not Hesaplama      ║")
    print("║  7-Carpim Tablosu     ║")
    print("║  8-BMI Hesaplama      ║")
    print("║  9-Fiyat Hesaplama    ║")
    print("║ 10-Cikis              ║")
    print("║   Seçiminiz nedir?    ║")
    print("╚═══════════════════════╝")
    print("\033[0m") 
     
    secim = int(input())
    print("Seçiminiz:",secim,"idi.")

    if secim < 1 or secim > 11:
        print("Secim yanlis. 1-10 arasi bir deger giriniz.")
        anamenu()

    elif secim == 1:
        print("Hesaplamalar uygulamasini seçtiniz.")
        import hesaplamalar
        hesaplamalar.hesapmenu()
        
    elif secim == 2: 
        print("Oyunlar uygulamasini seçtiniz.")
        import proje_oyunlar_menusu
        proje_oyunlar_menusu.oyun_menu()
    
    elif secim == 3:
        print("Cizimler uygulamasini seçtiniz.")
        import cizimler
        cizimler.cizim_menu()

    elif secim == 4:
        print("Rehber uygulamasini seçtiniz.")
        import rehber
        rehber.rehber_menu()

    elif secim == 5:
        print("Ehliyet uygunluk sorgulamayi seçtiniz.")
        import ehliyet_uygunluk
        ehliyet_uygunluk.ehliyet()

    elif secim == 6:
        print("Not hesaplama uygulamasini seçtiniz.")
        import not_hesaplama
        not_hesaplama.notlar()
    
    elif secim == 7:
        print("Carpim tablosunu seçtiniz.")
        import carpim_tablosu
        carpim_tablosu.carpim()

    elif secim == 8:
        print("BMI hesaplama uygulamasini seçtiniz.")
        import BMI_hesaplama
        BMI_hesaplama.bmi_hesapla()

    elif secim == 9:
        print("Toplam fiyat hesaplama uygulamasini seçtiniz.")
        import toplam_fiyat_hesaplama
        toplam_fiyat_hesaplama.toplam_fiyat_hesapla()

    elif secim == 10: 
        print("Programdan cikiliyor.")
    else:
        print ("Gecersiz secim. Lutfen bir sayi giriniz.")

    anamenu()

selamla()
anamenu()





