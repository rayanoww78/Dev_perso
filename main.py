from objectif import dev_perso

import tkinter as tk
from tkinter import messagebox

from humeur import Humeur


def enregistrer_humeur():
    humeur = entry_humeur.get()
    raison = entry_raison.get()
    Humeur(humeur,raison)
    messagebox.showinfo("Humeur enregistrée", f"Humeur : {humeur}\nRaison : {raison}")
    entry_humeur.delete(0, tk.END)
    entry_raison.delete(0, tk.END)

def enregistrer_objectif():
    objectif = entry_objectif.get()
    importance = entry_importance.get()
    deadline = entry_deadline.get()
    estimation = entry_estimation.get()
    dev_perso(objectif,importance,estimation,deadline)
    messagebox.showinfo("Objectif enregistré", f"Objectif : {objectif}\nImportance : {importance}\nDeadline : {deadline}\nEstimation : {estimation}h")
    entry_objectif.delete(0, tk.END)
    entry_importance.delete(0, tk.END)
    entry_deadline.delete(0, tk.END)
    entry_estimation.delete(0, tk.END)

# Interface principale
root = tk.Tk()
root.title("Mood & Goal Tracker")
root.geometry("400x500")

# Section humeur
tk.Label(root, text="Ton humeur du jour :").pack(pady=5)
entry_humeur = tk.Entry(root, width=40)
entry_humeur.pack()

tk.Label(root, text="Pourquoi cette humeur ?").pack(pady=5)
entry_raison = tk.Entry(root, width=40)
entry_raison.pack()

tk.Button(root, text="Enregistrer humeur", command=enregistrer_humeur).pack(pady=10)

# Séparateur
tk.Label(root, text="-" * 50).pack()

# Section objectif
tk.Label(root, text="Ton objectif du jour :").pack(pady=5)
entry_objectif = tk.Entry(root, width=40)
entry_objectif.pack()

tk.Label(root, text="Niveau d'importance :").pack(pady=5)
entry_importance = tk.Entry(root, width=40)
entry_importance.pack()

tk.Label(root, text="Deadline (ex: 2024-05-01) :").pack(pady=5)
entry_deadline = tk.Entry(root, width=40)
entry_deadline.pack()

tk.Label(root, text="Estimation en heures :").pack(pady=5)
entry_estimation = tk.Entry(root, width=40)
entry_estimation.pack()

tk.Button(root, text="Enregistrer objectif", command=enregistrer_objectif).pack(pady=10)

root.mainloop()

