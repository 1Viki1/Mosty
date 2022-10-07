import tkinter as tk
import random
win = tk.Tk()

#na canvas kladieme komponenty
canvas = tk.Canvas(win, width=400, height = 450, bg = "pink")  #bg = background
canvas.pack()

voda = []
zem = []
piczem = tk.PhotoImage(file = "ostrov0.png")
picvoda = tk.PhotoImage(file = "ostrov3.png")
obrazky = [tk.PhotoImage(file = "ostrov_kruh0.png"),tk.PhotoImage(file="ostrov_kruh1.png")]
mosty = [tk.PhotoImage(file = "ostrov1.png"),tk.PhotoImage(file="ostrov2.png")]

sirobr = 50 #šírka
vysobr = 50 #výška

pocitadlo = 1
peniaze= 0


def clik_switcher(e):
    global pocitadlo
    pocitadlo += 1
    #canvas.itemconfig("switcher",image=obrazky[pocitadlo%2])
    if pocitadlo%2 == 0:                 #canvas.itemcget("switcher", "image") == "pyimage3":
        canvas.itemconfig("switcher", image=obrazky[1])
    elif pocitadlo%2 == 1:       #canvas.itemcget("switcher", "image") == "pyimage4":
        canvas.itemconfig("switcher", image=obrazky[0])
    print(pocitadlo)


poc = 0
def skusadlo(e):      # e = event
    global pocitadlo, peniaze, poc
    x = e.x
    y = e.y
    idecko = canvas.find_withtag("current")[0]
    #print(idecko)
    canvas.delete(idecko)
    x = (e.x//50)*50
    y = (e.y//50)*50
    if canvas.itemcget("switcher", "image") == "pyimage3":
        canvas.create_image(x+24,y+24, image=mosty[0], tags="bridge")
        if poc%2 == 0:
            canvas.create_image(x+24,y+24, image=mosty[0], tags="bridge")
        if poc%2 ==1:
            canvas.create_image(x+24,y+24, image=mosty[1], tags="bridge")
        poc += 1
        peniaze += 10
    if canvas.itemcget("switcher", "image") == "pyimage4":
        canvas.create_image(x+24,y+24, image=piczem)
        peniaze += 50
    print(canvas.itemcget("switcher", "image"))

def create_screen():
    global zem
    m = random.randrange(4,7)  # randrange = vyberie aj čísla medyi týmito   randint = vyberie len medzi číslami v zátvorke
    n = random.randrange(3,10)
    for stlpec in range(n):
        for riadok in range(m):
            temp = random.randrange(1,6)
            if temp == 3:
                temp = canvas.create_image(riadok*sirobr, stlpec*vysobr, image = piczem, anchor = "nw")
                zem.append(temp)
            else:
                temp = canvas.create_image(riadok*sirobr, stlpec*vysobr, image = picvoda, anchor = "nw", tags = "water")
                zem.append(temp)
    canvas.create_image(400,10, anchor="ne", image=obrazky[0], tags="switcher")        # ne=>northwest


create_screen()
canvas.tag_bind("switcher", "<Button-1>",clik_switcher) #pripli sme udalosť nie na celý canvas ale na učité miesto + pripíname udalosť na objekty s konkrétnym tagom
canvas.tag_bind("water", "<Button-1>",skusadlo)
canvas.tag_bind("bridge", "<Button-1>",skusadlo)


text = canvas.create_text(330,35, text=peniaze, font = "Arial 20")

win.mainloop()
