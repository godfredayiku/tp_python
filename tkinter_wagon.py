from tkinter import *

fen1 = Tk()
fen1.title("Wagon")
c = Canvas (fen1, bg='ivory', height=130, width=535)

def cercle (can,x,y,r):
    can.create_oval(x-r,y-r,x+r,y+r)
    
def rectangle (can,x,y,larg,long):
    can.create_rectangle(x,y,x+larg,y+long)

def dessiner_wagon (can,x,y,larg,long) :
    rectangle(can,x,y,larg,long)
    for i in range (x+5,x+larg-24,35):
       rectangle(can,i,y+5,30,35)
        
    cercle (can,x+20,y+70,10)
    cercle (can,x+90,y+70,10)

dessiner_wagon (c, 10,30,110,60)
dessiner_wagon (c, 145,30,110,60)
dessiner_wagon (c, 280,30,110,60)
dessiner_wagon (c, 415,30,110,60)
c.pack()

fen1.mainloop()
