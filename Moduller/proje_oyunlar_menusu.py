
def oyun_menu():
    print("\033[1;33;40m")
    print("╔═════════════════════╗")
    print("║\033[1;35;40m    OYUNLAR MENU   \033[1;33;40m  ║")
    print("║                     ║")
    print("║  1-Tetris           ║")
    print("║  2-Adam asmaca      ║")
    print("║  3-Yilan            ║")
    print("║  4-Sayi Tahmin      ║")
    print("║  5-Sayi Toplama     ║")
    print("║  6-Ana menüye dön   ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    print("\033[0m") 

    ss = int(input())
    if ss == 1 : print("Tetris basliyor...")
    if ss == 2 : print("Adam asmaca basliyor...")
    if ss == 3 : 
        print("Yilan basliyor...")
        import snake
        snake.snake_game()
    if ss == 4 : 
        print("Sayi tahmin oyunu basliyor...")
        import sayi_tahmin
        sayi_tahmin.tahmin()  
    if ss == 5 : 
        print("Sayi toplama basliyor...")
        import sayi_toplama
        sayi_toplama.sayilar()
    if ss == 6 :
        import proje_ana_ekrani

oyun_menu()
    





