"""
3 užduotis
Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu", kuriame:

Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje,
kurioje spausdinamas pasisveikinimo tekstas
Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje
butų atspausdintas paskutinis atspausdintas tekstas
Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys

"""

from tkinter import *
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
#
# def antras():
#     print("Antras!")
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Isvalyti")
# submeniu.add_command(label="Atkurti", command=antras)
# submeniu.add_command(label="Iseiti",
# langas.mainloop()

from tkinter import *

langas = Tk('Labas, vardas uz aciu.')
langas.geometry("300x150")
kintamasis = StringVar()

def isvalyti():
    rezultatas["text"] = ""


def atkurti():
    rezultatas["text"] = kintamasis.get()

def iseiti():
    langas.destroy()


def spausdinti():
    ivesta = laukas.get()
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
laukas.bind("<Return>", lambda e: spausdinti())
mygtukas = Button(langas, text="Spausdinti", command=spausdinti)


rezultatas = Label(langas, text="")

uzrasas.grid(row=3, column=0, sticky=E)
laukas.grid(row=3, column=1)
mygtukas.grid(row=3, column=2)
rezultatas.grid(row=5, columnspan=3)


langas.mainloop()