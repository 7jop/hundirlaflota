from funciones import *
from variables import *
import pprint
import os
import time


#inicio del juego
mensaje_bienvenida()

#tablero del jugador
tablero= crear_tablero(dimensiones_tablero)

tablero_para_apuntar = crear_tablero(dimensiones_tablero)

#contador de casillas de barco tras preparar el tablero

#contador  =  numero_barcos_eslora1*1+numero_barcos_eslora2*2+numero_barcos3_eslora3*3+numero_barcos4_eslora4*4


#print("Tablero vacío")
#pprint.pprint(tablero)
posicionar_barcos_fijos(tablero)

posicionar_barcos_player(tablero_player)

#deshacer los dos siguientes comentarios para ver el tablero con los barcos enemigos
#print("Tablero computer con barcos fijos. Te doy 5 segundos para que los memorices...")
#visualizar(tablero)
#visualizar(tablero_player)
time.sleep(2)
#os.system("cls")
print()

#ciclo de turnos:
#acaba cuando uno de los jugadores gane
continuar=True

while continuar==True:
   
    continuar=turno_player(tablero)

    if continuar== False:
        print("Ganas")
        break
    else:
        print("")
    
    continuar=turno_maquina(tablero_player)


 
#cosas que podrían haberse hecho mejor si hubiera dispuesto de tiempo:
#1. posicionamiento aleatorio de barcos sin colisiones ni errores de out of bounds
#2. tablero bonito con tabulate o un módulo equivalente
#3. colores
#4. uso de caracteres ASCII/unicode 
#5. niveles de dificultad(inteligencia)
#6. revelar casillas circundantes tras disparo exitoso
#7. no hay excepciones en los inputs




