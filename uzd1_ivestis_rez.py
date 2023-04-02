"""
1 užduotis
Sukurti programą su grafine sąsaja, kuri:

Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus,
programa po lauku atspausdintų "Labas, {vardas}!"
"""

from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = laukas.get()
    rezultatas["text"] = f"Labas, {ivesta}!"

uzrasas = Label(langas, text="Iveskite varda")
laukas = Entry(langas)
mygtukas = Button(langas, text="Spausdinti", command=spausdinti)
rezultatas = Label(langas, text="")

uzrasas.grid(row=0, column=0, sticky=E)
laukas.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)


langas.mainloop()