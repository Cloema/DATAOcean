# coding: utf-8
import string
from tkinter import *

fenetre = Tk()

# FRAME name
lname = LabelFrame(fenetre, text="User", padx=20, pady=20)
lname.pack(fill="both", expand="yes")
Label(lname, text="Name").pack(side=LEFT)
entree = Entry(lname, textvariable=string, width=30)
entree.pack(side=RIGHT)

# FRAME name
lbouton = LabelFrame(fenetre, text="Choix", padx=20, pady=20)
lbouton.pack(fill="both", expand="yes")
# radiobutton
value = StringVar()
bouton1 = Radiobutton(lbouton, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(lbouton, text="Non", variable=value, value=2)
bouton3 = Radiobutton(lbouton, text="bien au contraire", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

# Scale
value = DoubleVar()
scale = Scale(fenetre, variable=value)
scale.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()