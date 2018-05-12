'''
En Abecelandia, ciudad famosa por sus N bellas plazas y que puede que conozcas, tienen 
un curioso sistema de carreteras: desde cada plaza sale una calle a todas las otras plazas 
que comienzan con una letra que se encuentre en su nombre (por ejemplo, de la plaza Aro 
salen calles que llevan a las plazas que empiezan por R, como las plaza Ruido y Reto, o 
por O, como la plaza Osa, pero no salen calles a plazas como Duende, Cascada o Tiara). 
Las calles son de sentido único (de la plaza Aro se puede ir a la plaza Ruido, pero no 
al revés ya que no cumple la regla de las letras; obviamente, otras plazas como Aro y Osa 
están conectadas entre sí en ambas direcciones). Todas estas conexiones entre las N plazas 
están recogidas en un callejero, representado por una matriz de adyacencia de tamaño NxN; 
así, el valor de Callejero[p, q] indica si se puede ir de la plaza p a la plaza q.

Se acerca el día 26 de Abril, festividad de San Isidoro de Sevilla (patrón de las Letras 
y, casualmente, de los informáticos), y en el Ayuntamiento de Abecelandia han decidido que 
para celebrarlo van a invertir la dirección de todas las calles que conectan sus plazas. 
En ese día no se podrá circular de Aro a Ruido, pero sí se permitirá ir de Ruido a Aro; 
obviamente, Aro y Osa seguirán conectadas entre sí.

Diseñar formalmente un algoritmo Divide y Vencerás estándar que, teniendo por dato el 
callejero de la ciudad (representado por la matriz de adyacencia), obtenga el nuevo 
callejero válido para el día de San Isidoro de Sevilla, indicando las estructuras de 
datos que se utilicen.
'''

import math

### FUNCTIONS ###

# PARA QUE EL METODO FUNCIONE LA MATRIZ DEBE TENER TAMAÑO DE POTENCIAS DE DOS
# RELLENAMOS CON COLUMNAS Y FILAS DE 0 HASTA LLEGAR AL TAMAÑO ADECUADO
def adaptarCallejero(callejero):
    exp = 1
    tamaño = 0
    while tamaño < len(callejero):
        tamaño = math.pow(2, exp)
        exp += 1
    
    diferencia = int(tamaño - len(callejero))
    ceros = [0] * diferencia # CEROS EXTRA EN CADA FILA COMO COLUMNAS
    for calle in callejero:
        calle.extend(ceros)
    
    ceros = [0] * len(callejero[0]) # FILAS DE CEROS EXTRA
    for i in range(diferencia):
        callejero.append(ceros)

# RECUPERAMOS EL TAMAÑO ORIGINAL QUITANDO ESAS COLUMNAS Y FILAS QUE HABIAMOS AÑADIDO
def recuperarCallejero(callejero, tamaño_original):
    diferencia = int(len(callejero) - tamaño_original)
    for calle in callejero:
        # ELIMINAMOS EL RESTO DE COLUMNAS DE CADA FILA
        del calle[len(calle) - diferencia:]

    # ELIMINAMOS EL RESTO DE FILAS
    del callejero[len(callejero) - diferencia:]

# METODO PARA DIVIDIR EN CUADRANTES LA MATRIZ Y TRANSPONER HASTA QUE SEA 2x2
def invertirCallejero(c, iini, jini, ifin, jfin):
    if ifin - iini < 2:
        # LLEGAMOS A MATRIZ 2x2, INTERCAMBIO MANUAL DE B Y C
        aux = c[iini][jfin]
        c[iini][jfin] = c[ifin][jini]
        c[ifin][jini] = aux
        return
    else:
        # PARTIMOS LA MATRIZ EN 4 CUADRANTES [A, B, C, D]
        imit = (ifin + iini) // 2
        jmit = (jfin + jini) // 2
        
        # Y TRANSPONEMOS CADA CUADRANTE
        invertirCallejero(c, iini, jini, imit, jmit)          #A
        invertirCallejero(c, iini, jmit + 1, imit, jfin)      #B
        invertirCallejero(c, imit + 1, jini, ifin, jmit)      #C
        invertirCallejero(c, imit + 1, jmit + 1, ifin, jfin)  #D

        # INTERCAMBIAMOS LOS CUADRANTES B Y C
        baux = [] # BACKUP B COMO VECTOR
        for i in range(iini, imit + 1):
            for j in range(jmit + 1, jfin + 1):
                baux.append(c[i][j])

        caux = [] # BACKUP C COMO VECTOR
        index = 0
        for i in range(imit + 1, ifin + 1):
            for j in range(jini, jmit + 1):  
                caux.append(c[i][j])
                c[i][j] = baux[index]  # INTERCAMBIAR: C <- B
                index += 1

        index = 0
        for i in range(iini, imit + 1):
            for j in range(jmit + 1, jfin + 1):
                c[i][j] = caux[index]  # INTERCAMBIAR: B <- C
                index += 1

        return


### MAIN ###

# CALLEJERO
# =========
############## Aro,     Ruido,   Reto,    Osa,     Duende,  Cascada, Tiara
########## Aro  1        1        1        1        0        0        0   
######## Ruido  0        1        1        1        1        0        0
######### Reto  0        1        1        1        0        0        1
########## Osa  1        0        0        1        0        0        0
####### Duende  0        0        0        0        1        0        0
###### Cascada  1        0        0        0        1        1        0
######## Tiara  1        1        1        0        0        0        1
callejero = [
    [1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1]
]

print('CALLEJERO')
for calle in callejero:
    print(calle)

tamaño_original = len(callejero)
adaptarCallejero(callejero)
invertirCallejero(callejero, 0, 0, len(callejero)-1, len(callejero)-1)
recuperarCallejero(callejero, tamaño_original)

print('26 ABRIL')
for calle in callejero:
    print(calle)
