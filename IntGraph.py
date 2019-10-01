from Tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        # FRAME name
        lname = LabelFrame(fenetre, text="Salinity", padx=20, pady=20)
        lname.pack(fill="both", expand="yes")
        Label(lname, text="Enter the salinity").pack(side=LEFT)
        salinity = Entry(lname, textvariable=float, width=30)
        salinity.pack(side=RIGHT)

        lname = LabelFrame(fenetre, text="Temperature", padx=20, pady=20)
        lname.pack(fill="both", expand="yes")
        Label(lname, text="Enter the temperature").pack(side=LEFT)
        temperature = Entry(lname, textvariable=float, width=30)
        temperature.pack(side=RIGHT)

        # Scale
        value = DoubleVar()
        scale = Scale(fenetre, variable=value)
        scale.pack()

        # bouton de sortie
        bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
        bouton.pack()

        fenetre.mainloop()
