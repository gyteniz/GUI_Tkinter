
"""
5 užduotis (papildoma)
Perdaryti bet kurią ankstesnėse pamokose sukurtą arba savo programą,
kurioje vartotojas turėjo įvesti duomenis, į programą su grafine sąsaja.
Pvz., tą, kuri atrenka keliamuosius metus, skaičiuoja laiką nuo praeitos datos,
pateikia informaciją apie įvestą eilutę ar pan.

"""
#

#
# def ar_keliemieji(metai):
#     return calendar.isleap(metai)
#
# print(ar_keliemieji(2100))

from tkinter import *
import calendar

langas = Tk()
langas.geometry("400x300")
langas.title("Keliamieji metai")
# langas.config(bg="none")

def ar_keliemieji(metai):
    return calendar.isleap(metai)


def keliamieji():
    try:
        metai = int(laukas.get())
        if ar_keliemieji(metai) is True:
            rezultatas["text"] = f"Ivesti {metai} metai yra keliamieji!"
        else:
            rezultatas["text"] = f"Ivesti {metai} metai yra nekeliamieji!"
        # break
    except ValueError:
        rezultatas["text"] = "Ivedete proshalini, neformalu,\n moraliskai neteisinga skaitmeni"





frame1= Frame(langas)
uzrasas = Label(frame1, text="Iveskite metus")
uzrasas.grid(row=0, column=0, sticky=E)

laukas = Entry(frame1)
laukas.grid(row=0, column=1)
laukas.bind("<Return>", lambda e: keliamieji())

mygtukas = Button(frame1, text="Rodyti", command=keliamieji)
mygtukas.grid(row=0, column=2)
frame1.pack(expand=True)


frame2= Frame(langas)
rezultatas = Label(frame2, text="")
rezultatas.grid(row=0, columnspan=3)
frame2.pack(expand=True)

langas.mainloop()