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
langas.geometry("400x300")
langas.title("Labas!")
langas.config(bg='#F2B33D')
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

    rezultatas["text"] = f"Labas, {ivesta}!"
    status["text"] = "Sukurta"
    kintamasis.set(rezultatas["text"])


meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Isvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Iseiti", command=iseiti)

frame = Frame(langas, bg='#F2B33D')

uzrasas = Label(frame, text="Iveskite varda", fg="white", bg="black").grid(row=3, column=0, sticky=E)
laukas = Entry(frame)
laukas.grid(row=3, column=1)
laukas.bind("<Return>", lambda e: spausdinti())
mygtukas = Button(frame, text="Spausdinti", command=spausdinti, fg="white", bg="black").grid(row=3, column=2)

rezultatas = Label(frame, text="", bg='#F2B33D')
rezultatas.grid(row=5, columnspan=3)

frame.pack(expand=True)

status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W, bg='#F2B33D')
status.pack(side=BOTTOM, fill=X)

langas.mainloop()
