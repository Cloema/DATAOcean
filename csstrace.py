#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import csv
import matplotlib.pyplot as plt

tempdata=[]
conddata=[]

xmin=0
xmax=10           #sera redéfini apres donc mettre n'importe quel valeurs initiale
tempmin=5
tempmax=25
condmin=10
condmax=50

fname = "datalog.csv"
file = open(fname, "r")

try:
    reader = csv.reader(file)

    for row in reader:
        tempdata.append(float(row[3]))
        conddata.append(float(row[4]))
        xmax=(len(tempdata))

    print(tempdata)
    print(conddata)

    plt.subplot(2, 1, 1, facecolor='y')
    plt.axis([xmin, xmax, tempmin, tempmax])
    plt.plot(tempdata)
    plt.title("Data Ocean")
    plt.ylabel("Temperature (°C)")
    plt.subplot(2, 1, 2, facecolor='c')
    plt.axis([xmin, xmax, condmin, condmax])
    plt.plot(conddata)
    plt.ylabel("Conduc (S/cm)")
    plt.xlabel("Time")
    plt.show()
    plt.close()

finally:
    file.close()       # Fermeture du fichier source
