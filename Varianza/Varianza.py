from math import sqrt

def desviacion_estandar(valores):    
    suma=0
    for x in valores:
        suma+=x
        print x
    prom=suma/float(len(valores))
    print prom
    suma_dif_cuadrado=0
    for x in valores:
        suma_dif_cuadrado+=(prom-x)**2
        print suma_dif_cuadrado
    varianza=suma_dif_cuadrado/float(len(valores)-1)
    return sqrt(varianza)

