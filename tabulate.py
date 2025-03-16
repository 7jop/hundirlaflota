from tabulate import tabulate

def crear_tablero(dimensiones_tablero):
    tablero = [["~" for i in range(dimensiones_tablero)] for j in range(dimensiones_tablero)]
    return tablero


tablero_player=crear_tablero(10)
print(tablero_player)




test=tabulate.tabulate(tablero_player)
#print(test)
