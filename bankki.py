from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

ikkuna = tk.Tk()
ikkuna.minsize(400, 400)
ikkuna.title("Manage accounts")
tabControl = ttk.Notebook(ikkuna)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Add account")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Search account")


tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Browse all accounts")

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text="Deposit/withdrawal")
tabControl.pack(expand=1, fill="both")

tilit = []


class Tili:
    def __init__(self, ID, nimi, raha):
        self.ID = ID
        self.nimi = nimi
        self.raha = raha



def add():
    tilit.append(Tili(tunnusentry.get(), nameentry.get(), moneyentry.get()))
    tunnusentry.delete(0, "end")
    nameentry.delete(0, "end")
    moneyentry.delete(0, "end")

    piirtotilit()


def piirtotilit():
    for tili in tilit:
        tili.tiliteksti = tk.Label(tab3, text=tili.ID)
        tili.nimiteksti = tk.Label(tab3, text=tili.nimi)
        tili.rahateksti = tk.Label(tab3, text=tili.raha)

        tili.tiliteksti.grid(row=tilit.index(tili)+1, column=0)
        tili.nimiteksti.grid(row=tilit.index(tili)+1, column=1)
        tili.rahateksti.grid(row=tilit.index(tili)+1, column=2)


def etsi():
    l = 0
    hakuid = identry.get()
    for tili in tilit:
        if(hakuid == tili.ID):
            tulos = "Account owner: "+tili.nimi+"\nAccount balance: "+tili.raha
            tk.messagebox.showinfo("Done.", tulos)
            l = 1
    if(l == 0):
        tk.messagebox.showinfo("Done.", "Not Found")

    identry.delete(0, "end")

def increase(x):
    jep = accentry.get()
    joo = summaentry.get()

    for tili in tilit:
        if(jep == tili.ID):
            if(x == 0):
                tili.raha = str(int(tili.raha) + int(joo))
            else:
                tili.raha = str(int(tili.raha) - int(joo))
            tk.messagebox.showinfo("Done.", str(tili.nimi)+" now has "+str(tili.raha))
    accentry.delete(0, "end")
    summaentry.delete(0, "end")
    piirtotilit()


# ADD ACCOUND TAB
tunnus = tk.Label(tab1, text="ID num.:")
tunnusentry = tk.Entry(tab1)
tunnus.grid(row=0, column=0)
tunnusentry.grid(row=0, column=1)

name = tk.Label(tab1, text="Name:")
nameentry = tk.Entry(tab1)
name.grid(row=1, column=0)
nameentry.grid(row=1, column=1)

money = tk.Label(tab1, text="Money amount:    ")
moneyentry = tk.Entry(tab1)
money.grid(row=2, column=0)
moneyentry.grid(row=2, column=1)

addnappi = tk.Button(tab1, text="ADD", command=add)
addnappi.grid(row=4, column=1)


# SEARCH TAB
haeid = tk.Label(tab2, text="ID number:")
identry = tk.Entry(tab2)
hakunappi = tk.Button(tab2, text="Search", command=etsi)
haeid.grid(row=0, column=0)
identry.grid(row=0, column=1)
hakunappi.grid(row=0, column=2)

# ALL ACCOUNTS TAB3
bid = tk.Label(tab3, text=" ID number ", font=("Helvetica", 12, "bold"))
bnimi = tk.Label(tab3, text=" Name ", font=("Helvetica", 12, "bold"))
bmoney = tk.Label(tab3, text=" Money amount ", font=("Helvetica", 12, "bold"))

bid.grid(row=0, column=0)
bnimi.grid(row=0, column=1)
bmoney.grid(row=0, column=2)

# MANAGE BALANCE TAB
valitseacc = tk.Label(tab4, text="Account ID:")
summa = tk.Label(tab4, text="Amount:")
accentry = tk.Entry(tab4)
summaentry = tk.Entry(tab4)


valitseacc.grid(row=0, column=0)
summa.grid(row=1, column=0)
accentry.grid(row=0, column=1)
summaentry.grid(row=1, column=1)

addnappi = tk.Button(tab4, text="Deposit", command=lambda: increase(0))
remnappi = tk.Button(tab4, text="Withdraw", command=lambda: increase(1))

addnappi.grid(row=2, column=0)
remnappi.grid(row=2, column=1)

ikkuna.mainloop()
