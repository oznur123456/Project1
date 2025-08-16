def cizim_menu():
    print("\033[1;33;40m")
    print("╔═════════════════════╗")
    print("║\033[1;35;40m     CIZIM MENU    \033[1;33;40m  ║")
    print("║                     ║")
    print("║  1-Kare             ║")
    print("║  2-Dikdortgen       ║")
    print("║  3-Ucgen            ║")
    print("║  4-Cemberler        ║")
    print("║  5-Sekizgen         ║")
    print("║  6-Ana menüye dön   ║")
    print("║                     ║")
    print("║  Seçiminiz nedir?   ║")
    print("╚═════════════════════╝")
    print("\033[0m") 

    s = int(input("Seçiminiz?"))
    if s== 1: kareciz()
    elif s== 2: dikdortgenciz()
    elif s== 3: ucgenciz()
    elif s== 4: cemberciz()
    elif s== 5: sekizgenciz()
    elif s == 6:
        import proje_ana_ekrani
    
def kareciz():
    import turtle
    for xx in range(4):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    cizim_menu()

def dikdortgenciz():
    import turtle
    for xx in range(4):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
    cizim_menu()

def ucgenciz():
    import turtle
    for a in range(3):
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
    cizim_menu()
       
def cemberciz():
    import turtle
    turtle.speed(9)
    for i in range(11):
        turtle.circle(i)
        turtle.forward(20)
    cizim_menu()

def sekizgenciz():
    import turtle
    t = turtle.Turtle()
    for i in range(8):
        t.forward(50)
        t.left(45)
    cizim_menu()


cizim_menu()