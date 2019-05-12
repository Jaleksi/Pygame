import tkinter as tk
from tkinter import messagebox
from random import randint

ikkuna = tk.Tk()
ikkuna.minsize(200, 200)
ikkuna.title("Minaharv")
napit = []
koko = 20
vaikeus = 6
tmp = []
class Nappi:
    def __init__(self, x, y, pommi):
        self.x = x
        self.y = y
        self.pommi = pommi
        self.vari = "gray88"
        self.tx = "  "
        self.avattu = 0
        self.nro = 0

    def valikko():
        menubar = tk.Menu(ikkuna)
        ikkuna.config(menu=menubar)
        valinta = tk.Menu(menubar)
        menubar.add_cascade(label="Uusi peli", menu=valinta)
        valinta.add_command(label="Aloita", command=Nappi.aloitus)

        vaikeus = tk.Menu(menubar)
        menubar.add_cascade(label="Vaikeus", menu=vaikeus)
        vaikeus.add_command(label="Helppo", command=lambda: Nappi.vaikeus(1))
        vaikeus.add_command(label="Normaali", command=lambda: Nappi.vaikeus(2))
        vaikeus.add_command(label="Vaikea", command=lambda: Nappi.vaikeus(3))

    def vaikeus(x):
        global koko
        global vaikeus

        if(x == 1):
            koko = 10
            vaikeus = 8
        elif(x == 2):
            koko = 20
            vaikeus = 6
        elif(x == 3):
            koko = 20
            vaikeus = 3

    def piirto(self):
        global tmp
        self.tx = str(self.naapurit())
        if(self.avattu == 1):
            if(self.pommi == 0):
                self.tx = "*"
                self.vari = "red"
            else:
                self.vari = "white"
            if(self.tx == "0"):
                self.tx = "  "
            self.button = tk.Button(ikkuna, bg=self.vari,text=self.tx)
            self.button.bind("<Button-1>", self.klik)  #command=self.klik
            self.button.bind("<Button-3>", self.liputus)
            self.button.grid(row=self.x, column=self.y)
            tmp.append(self.button)

        else:
            self.button = tk.Button(ikkuna, text="  ", bg=self.vari)
            self.button.bind("<Button-1>", self.klik)
            self.button.bind("<Button-3>", self.liputus)
            self.button.grid(row=self.x, column=self.y)
            tmp.append(self.button)

    def liputus(self, event):
        if(self.vari != "red" and self.avattu == 0):
            self.vari = "red"
        elif(self.vari == "red" and self.avattu == 0):
            self.vari = "gray88"
        self.piirto()

    def klik(self, event):
        if(self.pommi == 0):
            for nappi in napit:
                nappi.avattu = 1
                nappi.piirto()
        self.avattu = 1
        self.piirto()
        if(self.nro == 0):
            self.nollaus()
        if(self.pommi == 0):
            Nappi.havio()
        if(self.pommi != 0):
            Nappi.tarkistus()

    def naapurit(self):
        naapuripommit = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for nappi in napit:
                    if(nappi.x == (self.x + i) and nappi.y == (self.y + j)):
                        if(nappi.pommi == 0 and nappi != self):
                            naapuripommit += 1

        self.nro = naapuripommit
        return naapuripommit

    def nollaus(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                for nappi in napit:
                    if(nappi.x == (self.x + i) and nappi.y == (self.y + j)):
                        if(self.nro == 0 and nappi.nro == 0 and nappi.avattu == 0):
                            nappi.avattu = 1
                            nappi.piirto()
                            nappi.nollaus()
                        elif(self.nro == 0  and nappi.avattu == 0):
                            nappi.avattu = 1
                            nappi.piirto()


    def aloitus():
        global tmp
        for button in tmp:
            button.destroy()
        napit.clear()
        for i in range(koko):
            for j in range(koko):
                napit.append(Nappi(i, j, randint(0, vaikeus)))
        for nappi in napit:
            nappi.piirto()

    def tarkistus():
        bombs = 0
        for nappi in napit:
            if(nappi.avattu == 0 and nappi.pommi != 0):
                bombs += 1
        if(bombs == 0):
            Nappi.voitto()


    def voitto():
        tk.messagebox.showinfo("Voitto!", "Hienosti pelattu.")

    def havio():
        tk.messagebox.showinfo("Häviö!", "Huonosti pelattu.")


Nappi.aloitus()

Nappi.valikko()
ikkuna.mainloop()
