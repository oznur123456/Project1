
def oyunmenu():
    print("\033[1;33;40m")
    print("╔═════════════════════╗")
    print("║\033[1;35;40m     OYUN MENUSU   \033[1;33;40m  ║")
    print("║                     ║")
    print("║  1-Tetris           ║")
    print("║  2-Adam asmaca      ║")
    print("║  3-Yilan            ║")
    print("║  4-                 ║")
    print("║  5-                 ║")
    print("║  6-Ana menüye dön   ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
    ss = input()
    if ss == "1" : print("Tetris başlıyor..")
    if ss == "6":
        import proje_ana_ekrani

oyunmenu()
    



