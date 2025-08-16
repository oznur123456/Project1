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
    print("║  6-Rastgele kareler ║")
    print("║  7-Rastgele sekiller║")
    print("║  8-Ana menüye dön   ║")
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
    elif s== 6: rastgeleciz()
    elif s== 7: rastgele_sekiller()
    elif s == 8:
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

def rastgeleciz():
    import random as r, turtle as t
    t.speed(10)
    for b in range(r.randint(5,20)):
        renkler = ["olive","green","sky blue", "violet", "orange", "red", "magenta"]
        ku = r.randint(50,150)
        x = r.randint(-300,300)
        y = r.randint(-300,300)
        t.color(r.choice(renkler))
        t.up() # t.penup()
        t.goto(x,y)
        t.down()
        for a in range(4):
            t.forward(ku)
            t.right(90)
    input()
    cizim_menu()


import random as r, turtle as t
def rastgele_sekiller():
    t.speed(10)
    for b in range(r.randint(5,20)):
        renkler = ["magenta", "black", "purple", "red","green","blue"]
        ku = r.randint(50,150)
        x = r.randint(-300,300)
        y = r.randint(-300,300)
        t.color(r.choice(renkler))
        t.up() 
        t.goto(x,y)
        t.down()
        ks = r.randint(3,7)
        for a in range(ks):
            t.forward(ku)
            t.right(360/ks)
    input()
    cizim_menu()


cizim_menu()