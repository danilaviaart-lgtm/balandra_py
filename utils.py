# IMPORTAR MODULOS

import numpy as np
import random
import time
import sys

# COMENZAR JUEGO CON TABLEROS

def inicializar_juego():
    # Creamos los tableros
    p1_tablero = crea_tablero()
    p1_tablero_p2 = p1_tablero.copy()
    p2_tablero = p1_tablero.copy()
    p2_tablero_p1 = p1_tablero.copy()

    # Crea los barcos
    barcos = [2, 2, 3, 3, 4, 4]
    for i in barcos:
        p1_tablero = crea_barco_aleatorio(p1_tablero, i)
        p2_tablero = crea_barco_aleatorio(p2_tablero, i)
    
    return p1_tablero, p1_tablero_p2, p2_tablero, p2_tablero_p1

# CREAR TABLERO

def crea_tablero(lado = 10):
    tablero = np.full((lado,lado),"_")
    return tablero

# FUNCION DE DISPARO CON ERRORES

def disparo(coord1, coord2, p2_tablero, p1_tablero_p2):
    while True:
        if coord1.isdigit() and coord2.isdigit():
            if 1 <= int(coord1) <= 10 and 1 <= int(coord2) <= 10:
                break
        print("¡Capitán! Las coordenadas deben ser NÚMEROS entre 1 y 10.")
        coord1 = input("Introduce una nueva fila (1-10): ")
        coord2 = input("Introduce una nueva columna (1-10): ")
    
    coordenadas = int(coord1) - 1, int(coord2) - 1 # con esto arreglamso que sea más amigacle de 1 a 10 y no de 0 a 9
    acertado = recibir_disparo(p2_tablero, p1_tablero_p2, coordenadas)
    return acertado

# FUNCION GESTIONA DISPAROS

def recibir_disparo(tablero, t_jugador, coordenada):
    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        t_jugador[coordenada] = "X"
        print("Tocado")
        return True 
    elif t_jugador[coordenada] in ["X", "A"]:
        print("Agonia, deja de perder el tiempo, dispara a otro sitio")
        return False 
    else:
        tablero[coordenada] = "A"
        t_jugador[coordenada] = "A"
        print("Agua")
        return False

#  COLOCA BARCOS EN EL TABLERO SELECCIONADO

def coloca_barco_plus(tablero, barco):
    tablero_temp = tablero.copy()
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            return False
        if columna <0 or columna>= num_max_columnas:
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

#  GENERADOR DE BARCOS

def crea_barco_aleatorio(tablero,eslora = 4):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    while True:
        barco = []
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp


#  GENERA COORDENADAS PARA LA CPU

def generador_coord():
    x = np.random.randint(0,10) # Ajustado a 10 para evitar errores de índice
    y = np.random.randint(0,10)
    return int(x), int(y)

#  PRINT LENTO PARA EL TOQUE ANTIGUO

def print_lento(texto, velocidad=0.01):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()