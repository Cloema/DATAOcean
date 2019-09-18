# Operation de calcul de la salinité
# Etat : formule brute copier ici, il faut l'adapter au code

A =	[0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081]
B = [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144]
C = [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09]
K = 0.0162

def salinity_calculator(temperature, conductivity):
    R_p = 1. # pour les mesures à faible profondeur
    r_t = sum(
        [C[i] * temperature**i for i in range(5)]
    )
    R_t = conductivity / (42.914 * r_t)

    return (
        sum([A[i] * R_t**(int(i)/2.) for i in range(6)])
        + (
            ((temperature - 15)/(1 + K * (temperature - 15)))
            * (sum([B[i] * R_t**(int(i)/2.) for i in range(6)]))
        )
    )
