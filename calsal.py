# -*- coding: utf-8 -*-
# calsal.py
# author: CRI students
# date : september 2019
# version : V1.0


# Operation de calcul de la salinité
# Etat : formule brute copier ici, il faut l'adapter au code

'''
#Classe Calcul_salin for fun
'''
class Calcul_salin(object):
    def __init__(self):
        self.salin_test = []
        self.A = [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081]
        self.B = [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144]
        self.C = [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09]
        self.K = 0.0162

    def salinity_calculator(self,temperature, conductivity):
        R_p = 1. # pour les mesures à faible profondeur
        r_t = sum(
            [self.C[i] * temperature**i for i in range(5)]
        )
        R_t = conductivity / (42.914 * r_t)

        res =  (
            sum([self.A[i] * R_t**(int(i)/2.) for i in range(6)])
            + (
                ((temperature - 15)/(1 + self.K * (temperature - 15)))
                * (sum([self.B[i] * R_t**(int(i)/2.) for i in range(6)]))
            )
        )
        self.salin_test.append(res)
        print("I AM IN THE FUNCTION : " , res)
        return res
