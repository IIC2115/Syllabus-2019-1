#######################
## LIBRERIA COMODORO ##
#######################
# No realizar modificaciones en este archivo
# Acentos omitidos

# Paquetes necesarios
import matplotlib.pyplot as plt
import copy
import numpy as np
from random import randint
import csv

# Funcion que genera un mapa en base a la informacion de la 
# carpeta mapas (esta debe estar en la misma carperta que este archivo)
# nMapa (int): indicar el numero de mapa a utilizar  
def generar_mapa(nMapa):
    results = []
    filename = 'mapas/mapa{}.csv'.format(nMapa)
    results = []
    try:
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                results.append(row)
    except:
        print('Error de archivo, verificar el formato o que el archivo exista')
    
    return results

# Funcion que imprime graficamente el estado de la red
# personas (list of lists): corresponde al archivo con la cantidad de personas por celda
# vialidad (list of lists): corresponde al archivo de vialidad entregado por generar_mapa()
def imprimir_mapa(personas, vialidad):
    plot = copy.deepcopy(personas)
    for i in range(0,len(vialidad)):
        for j in range(0,len(vialidad[i])):
            if vialidad[i][j] == -1 or vialidad[i][j] == 0 or vialidad[i][j] == 1:
                plot[i][j] = -100
    plt.imshow(plot, cmap='rainbow', interpolation='nearest')
    plt.show()

# Entrega un numero uniforme entre a y b    
def uniforme(a,b):
    rnd = np.random.uniform(a,b)
    return rnd

# Entrega un valor exponencial con tasa lamda
def exponencial(lamda):
    rnd = np.random.exponential(lamda)
    return rnd

# Entrega la decision de ruta, se deben indicar las opciones disponibles
# a: arriba; b: abajo; i:izquierda; d:derecha (todos son bool)
# True si esta disponible, False si no
def ruta(a, b, i, d):
    opciones = {'a':a,'b':b,'i':i,'d':d}
    posibles = [op for op in opciones if opciones[op]]
    eleccion = randint(0, len(posibles)-1)
    return posibles[eleccion]
