
"""
2 užduotis
Patobulinti 1 užduoties programą, kad ji:
Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"

"""
from tkinter import *

langas = Tk()

def spausdinti():
    ivesta = laukas.get()

    rezultatas["text"] = f"Labas, {ivesta}!"

uzrasas = Label(langas, text="Iveskite varda")
laukas = Entry(langas)
laukas.bind("<Return>", lambda e: spausdinti())
mygtukas = Button(langas, text="Spausdinti", command=spausdinti)


rezultatas = Label(langas, text="")

uzrasas.grid(row=0, column=0, sticky=E)
laukas.grid(row=0, column=1)
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)


langas.mainloop()