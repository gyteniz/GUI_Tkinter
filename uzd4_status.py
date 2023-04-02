"""
4 užduotis
Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:

Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas Nuspaudus
klaviatūros mygtuką "Escape", uždarytų programos langą
"""
from tkinter import *

langas = Tk('Labas, vardas uz aciu.')
langas.geometry("280x70")
kintamasis = StringVar()

def isvalyti():
    rezultatas["text"] = ""
    status["text"] = "Isvalyta"

def atkurti():
    rezultatas["text"] = kintamasis.get()
    status["text"] = "Atkurta"

def iseiti():
    langas.destroy()


def spausdinti():
    ivesta = laukas.get()
    status["text"] = "Sukurta"
    rezultatas["text"] = f"Labas, {ivesta}!"
    kintamasis.set(rezultatas["text"])



meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Isvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Iseiti", command=iseiti)

uzrasas = Label(langas, text="Iveskite varda")
laukas = Entry(langas)
print(type(laukas))
laukas.bind("<Return>", lambda e: spausdinti())
mygtukas = Button(langas, text="Spausdinti", command=spausdinti)
rezultatas = Label(langas, text="")

status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)



uzrasas.grid(row=3, column=0, sticky=E)
laukas.grid(row=3, column=1)
mygtukas.grid(row=3, column=2)
rezultatas.grid(row=5, columnspan=3)
status.grid(row=9, columnspan=3, sticky=W+E)






langas.mainloop()