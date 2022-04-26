from tkinter import *

def cercle(can, x, y, r):
    can.create_oval(x-r, y-r, x+r, y+r)


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.can = Canvas(self, bg = "ivory", height = 130, width = 535)
        self.can.pack(side = TOP, padx = 5, pady = 5)
        Button(self, text = "Train", command = self.dessiner).pack(side = LEFT)
        Button(self, text = "Bonjour", command = self.dessiner_personne).pack(side = LEFT)

    def dessiner(self):
        self.w1 = Wagon(self.can, 10, 30)
        self.w1 = Wagon(self.can, 145, 30)
        self.w1 = Wagon(self.can, 280, 30)
        self.w1 = Wagon(self.can, 415, 30)

    def dessiner_personne(self):
        self.w1.personne()
        


class Wagon():
    def __init__(self, can, x, y):
        self.can, self.x, self.y = can, x, y
        can.create_rectangle(x, y, x+110, y+60)
        for i in range(x+5, x+86, 35):
            can.create_rectangle(i, y+5, i+30, y+35)

        cercle(can, x+20, y+70, 10)
        cercle(can, x+90, y+70, 10)

    def personne(self):
        x1 = 30
        y1 = 50
        r1 = 10
        cercle(self.can, x1, y1, r1)
        cercle(self.can, x1, y1+5, r1-7)
        cercle(self.can, x1-4, y1-3, r1-8)
        cercle(self.can, x1+4, y1-3, r1-8)

app = Application()
app.mainloop()
