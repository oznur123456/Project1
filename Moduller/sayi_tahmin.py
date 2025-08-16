def tahmin():

    import random as r 

    print("SAYI TAHMIN OYUNU")
    min = 1
    max = 100
    hak = 10
    puan = 100    

    tutulan = r.randint(min, max)
    print(f"Ben {min} ile {max} arasinda bir sayi tuttum.\n{hak} hakkin var.")

    for a in range(hak):
        tahmin = int(input("Tahminin nedir? "))

        if tahmin == tutulan:
            print("Aferin, bildin!")
            print ("Simdi oyunlar menusune yonlendiriliyorsunuz.")
            import proje_oyunlar_menusu
        elif tahmin > tutulan:
            puan -= 100 / hak
            print("Tahminin tutulan sayidan büyük.")
        elif tahmin < tutulan:
            puan -= 100 / hak
            print("Tahminin tutulan sayidan küçük.")
        else:
            print(f"Hakkin bitti. Tutulan sayi {tutulan} idi.")

    print(f"Oyun bitti. Puanin: {int(puan)}. Simdi oyunlar menusune yonlendiriliyorsunuz.")
    import proje_oyunlar_menusu

tahmin()