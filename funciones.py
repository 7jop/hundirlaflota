
from variables import *

import pprint
import time
import os
import random


#función para disparar
#no incluye tiro extra tras acertar(de momento)
def disparo(tablero,i,j):
    acierto=False
    if tablero[i][j]=="B":
        print("¡hemos acertado!")
        
        tablero[i][j]= "X"
        acierto=True
    elif tablero[i][j]== " ":
        print("agua!")
        tablero[i][j]="o"
        
    else:
        print("ya habías disparado allí, grumete")
    
    return conteo(tablero), acierto
    



def crear_tablero(dimensiones_tablero):
    tablero = [[" " for i in range(dimensiones_tablero)] for j in range(dimensiones_tablero)]
    return tablero

#para colocar barcos de forma manual y no aleatoria
def posicionar_barcos_fijos(tablero):
    tablero[0][0] = 'B'
    tablero[0][1] = 'B'

    tablero[1][3] = 'B'

    tablero[0][5] = 'B'

    tablero[1][7] = 'B'
    tablero[1][8] = 'B'

    tablero[3][1] = 'B'
    
    
    tablero[3][4] = 'B'
    tablero[3][5] = 'B'
    tablero[3][6] = 'B'
    tablero[3][7] = 'B'

    tablero[4][9] = 'B'
    tablero[5][9] = 'B'
    tablero[6][9] = 'B'

    tablero[7][2] = 'B'
    tablero[7][3] = 'B'

    tablero[7][5] = 'B'

    tablero[9][4] = 'B'
    tablero[9][5] = 'B'
    tablero[9][6] = 'B'

#colocación manual de barcos para el tablero sobre el que dispara la máquina

def posicionar_barcos_player(tablero):
    tablero[0][0]= 'B'
    
    tablero[2][0]= 'B'
    
    tablero[4][0]= 'B'
    tablero[5][0]= 'B'
    tablero[6][0]= 'B'
    tablero[7][0]= 'B'

    tablero[0][2]= 'B'
    tablero[1][2]= 'B'

    tablero[4][3]= 'B'

    tablero[6][3]= 'B'
    tablero[7][3]= 'B'
    tablero[8][3]= 'B'

    tablero[3][5]= 'B'
    tablero[3][6]= 'B'

    tablero[1][7]='B'
    tablero[1][8]='B'
    tablero[1][9]='B'

    tablero[5][7]='B'
    tablero[5][8]='B'

    tablero[8][7]='B'


#def posicionar_barcos_enemigos(tablero):

#para contar las casillas con barcos tras colocarlos en el tablero y en caso de que no haya ninguna, se acaba el juego

def conteo(tablero):
    
    contador=0
    for i in range(len(tablero)):
        
        for j in range(len(tablero)):
       
            if tablero[i][j]=="B":
                contador=contador+1
                #print(contador)
        
    return contador




#funciones para los turnos

#tableros
tablero= crear_tablero(dimensiones_tablero)

tablero_para_apuntar = crear_tablero(dimensiones_tablero)


#tablero sobre el que dispara el enemigo
tablero_player=crear_tablero(10)


#función del turno del jugador
def turno_player(tablero):

    game=True



    while True:
    
        
        
        print("Tus disparos")
        visualizar(tablero_para_apuntar)
        print("")
        i = int(input("Introduce la fila, por favor: "))
        j = int(input("Introduce la columna, por favor: "))
    
        contadorbarcos,acierto  =  disparo(tablero,i,j)
        
        
        
        tablero_para_apuntar[i][j]=tablero[i][j]
        


        

        
        if not acierto:
            break
        #os.system("cls")
        
        #winning condition:
        if contadorbarcos==0:
            print("~"*10)
            print("You win!")
            print("~"*10)
            pprint.pprint(tablero)
            #variable que termina con el juego
            game=False
            #return game
            break
    #print(game==True)
    print("")
    return game


#función de turno de la máquina

def disparo_enemigo(tablero,i,j):
    acierto=False
    print(f"¡Ataque en fila {[i]}, columna {[j]}")
    if tablero[i][j]=="B":
        print("¡el enemigo nos ha alcanzado!")
        
        tablero[i][j]= "X"
        acierto=True
    elif tablero[i][j]== " ":
        print("¡el enemigo ha fallado!")
        tablero[i][j]="o"
        
    else:
        print("el enemigo está desperdiciando su munición")
    
    return conteo(tablero_player), acierto






#def turno_maquina(tablero):
def turno_maquina(tablero):
   
    game=True
   
    while True:

        
        
        print("¡Disparo enemigo en camino!")
        visualizar(tablero_player)
        for i in range(0,3):
            print(".",end="")
            time.sleep(0.75)
        time.sleep(0.75)
        print("")

        i = random.randint(0,9)
        j = random.randint(0,9)
        while tablero[i][j]=="o":
            i = random.randint(0,9)
            j = random.randint(0,9)
        

        #disparo enemigo aleatorio
        # print(i,j)

        contadorbarcos,acierto  =  disparo_enemigo(tablero_player,i,j)
        #os.system("cls")
        visualizar(tablero_player)
        
        if not acierto:
           
            break
            
    
        
        #winning condition:
        if contadorbarcos==0:
            print("x"*10)
            print("You lose!")
            print("x"*10)
            game=False
            break
            
    return game





    
    




    
    
    
    
def visualizar(tablero):
    pprint.pprint(tablero)
    

#mensaje inicial al ejecutar el código   
def mensaje_bienvenida():
    print("--------------------------------------")
    print("Bienvenido al juego de hundir la flota")
    print("--------------------------------------")


    




    
    
    

    
    





