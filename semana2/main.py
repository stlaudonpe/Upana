tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

simbolo1 = ""
simbolo2 = ""

hay_ganador = False

turno_actual = True

# print(tablero)


def imprimir_tablero(tablero):
    print("Este es el tablero actual: ")
    tablero_cadena = ""
    for fila in tablero:
        for celda in fila:
            tablero_cadena = tablero_cadena + str(celda)
            tablero_cadena = tablero_cadena + " "
        tablero_cadena = tablero_cadena + "\n"
    print(tablero_cadena)
    return


def imprimir_instrucciones():
    print(
        """
Bienvenido a Totito.
    Cada turno, un jugador elige una posición vacía para colocar una pieza
    El primero en colocar tres piezas seguidas, gana.
    Los turnos se alternan
          """
    )


def juego_terminado(tablero):
    # Revisar fila
    for fila in tablero:
        if len(set(fila)) == 1 and all([x != 0 for x in fila]):
            return True
    # Revisar columna
    for i in range(3):
        columna = [tablero[0][i], tablero[1][i], tablero[2][i]]
        if len(set(columna)) == 1 and all([x != 0 for x in columna]):
            return True

    # Revisar diagonales
    diagonal1 = [tablero[0][0], tablero[1][1], tablero[2][2]]
    if len(set(diagonal1)) == 1 and all([x != 0 for x in diagonal1]):
        return True
    diagonal2 = [tablero[0][2], tablero[1][1], tablero[2][0]]
    if len(set(diagonal2)) == 1 and all([x != 0 for x in diagonal2]):
        return True

    hay_vacio = False
    for fila in tablero:
        for celda in fila:
            if celda == 0:
                hay_vacio = True
    if not hay_vacio:
        return True

    return False  # True o False


def jugada_legal(tablero, nuevo_fila, nueva_columna):
    # if tablero[nuevo_fila][nueva_columna] == 0:
    #    return True
    # return False
    return not tablero[nuevo_fila][nueva_columna]


imprimir_instrucciones()
imprimir_tablero(tablero)

simbolo1 = input("Jugador 1, ingrese su símbolo: ")
simbolo2 = input("Jugador 2, ingrese su símbolo: ")

while not juego_terminado(tablero):
    try:
        ingreso_x = int(input("Ingrese su fila: ")) - 1  # 1
        ingreso_y = int(input("Ingrese su columna: ")) - 1  # 2
        # 0 A 0
        # 0 0 0
        # 0 0 0
        if jugada_legal(tablero, ingreso_x, ingreso_y):
            tablero[ingreso_x][ingreso_y] = simbolo1 if turno_actual else simbolo2
            turno_actual = not turno_actual
            imprimir_tablero(tablero)
        else:
            print("Jugada ilegal, intente nuevamente")
    except:
        print("Algo salió mal, intente nuevamente")

print("Ya ha terminado el juego")

# Este es el tablero actual:
# 0 0 0
# 0 0 0
# 0 0 0
# \n
