import tkinter as tk
from tkinter import ttk, messagebox


def nb_felfele(a, b):
    db = int(a / b)
    if db < a / b:
        db += 1
    return db


def nb_csempe_darab(szoba_a, szoba_b, csempe_a, csempe_b):
    return nb_felfele(szoba_a, csempe_a) * nb_felfele(szoba_b, csempe_b)


def nb_visszajelzes(szukseges, meglevo):
    if meglevo >= szukseges:
        return f'Elég a csempe, {meglevo - szukseges} db marad.'
    return f'Nem elég, még {szukseges - meglevo} db-ot kell vásárolni.'


class NBCsempeSzamolo:
    def __init__(self, root):
        self.root = root
        self.root.title('Csempeszámoló')
        self.root.geometry('450x350')

        self.szoba_a = tk.StringVar()
        self.szoba_b = tk.StringVar()
        self.csempe_a = tk.StringVar()
        self.csempe_b = tk.StringVar()
        self.meglevo = tk.StringVar()

        self.szoba_a_cimke = ttk.Label(root, text='Szoba szélessége (cm)')
        self.szoba_a_cimke.grid(row=0, column=0, padx=10, pady=5)
        self.szoba_a_be = ttk.Entry(root, textvariable=self.szoba_a, width=10)
        self.szoba_a_be.grid(row=0, column=1, padx=10, pady=5)

        self.szoba_b_cimke = ttk.Label(root, text='Szoba hossza (cm)')
        self.szoba_b_cimke.grid(row=1, column=0, padx=10, pady=5)
        self.szoba_b_be = ttk.Entry(root, textvariable=self.szoba_b, width=10)
        self.szoba_b_be.grid(row=1, column=1, padx=10, pady=5)

        self.csempe_a_cimke = ttk.Label(root, text='Csempe szélessége (cm)')
        self.csempe_a_cimke.grid(row=2, column=0, padx=10, pady=5)
        self.csempe_a_be = ttk.Entry(root, textvariable=self.csempe_a, width=10)
        self.csempe_a_be.grid(row=2, column=1, padx=10, pady=5)

        self.csempe_b_cimke = ttk.Label(root, text='Csempe hossza (cm)')
        self.csempe_b_cimke.grid(row=3, column=0, padx=10, pady=5)
        self.csempe_b_be = ttk.Entry(root, textvariable=self.csempe_b, width=10)
        self.csempe_b_be.grid(row=3, column=1, padx=10, pady=5)

        self.meglevo_cimke = ttk.Label(root, text='Meglévő csempe (db)')
        self.meglevo_cimke.grid(row=4, column=0, padx=10, pady=5)
        self.meglevo_be = ttk.Entry(root, textvariable=self.meglevo, width=10)
        self.meglevo_be.grid(row=4, column=1, padx=10, pady=5)

        self.szamol_gomb = ttk.Button(root, text='Számol', command=self.szamol)
        self.szamol_gomb.grid(row=5, column=0, padx=10, pady=10)

        self.torol_gomb = ttk.Button(root, text='Törlés', command=self.torol)
        self.torol_gomb.grid(row=5, column=1, padx=10, pady=10)

        self.kilepes_gomb = ttk.Button(root, text='Kilépés', command=root.destroy)
        self.kilepes_gomb.grid(row=5, column=2, padx=10, pady=10)

        self.eredmeny = ttk.Label(root, text='Eredmény', font='Arial 12 bold')
        self.eredmeny.grid(row=6, column=0, padx=10, pady=10)

    def kiir(self, szoveg):
        self.eredmeny.config(text=szoveg)

    def szamol(self):
        try:
            szoba_a_cm = int(self.szoba_a.get())
            szoba_b_cm = int(self.szoba_b.get())
            csempe_a_cm = int(self.csempe_a.get())
            csempe_b_cm = int(self.csempe_b.get())
            meglevo_db = int(self.meglevo.get())
        except ValueError:
            messagebox.showerror('Hiba', 'Nem sikerül számmá átalakítani!')
            return

        if szoba_a_cm <= 0 or szoba_b_cm <= 0 or csempe_a_cm <= 0 or csempe_b_cm <= 0 or meglevo_db < 0:
            messagebox.showerror('Hiba', 'A méretek legyenek nagyobbak 0-nál!')
            return

        szukseges = nb_csempe_darab(szoba_a_cm, szoba_b_cm, csempe_a_cm, csempe_b_cm)
        self.kiir(f'Szükséges: {szukseges} db\n{nb_visszajelzes(szukseges, meglevo_db)}')

    def torol(self):
        self.szoba_a.set('')
        self.szoba_b.set('')
        self.csempe_a.set('')
        self.csempe_b.set('')
        self.meglevo.set('')
        self.kiir('Eredmény')
