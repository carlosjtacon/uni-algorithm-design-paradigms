'''
In Abcland, a city famous for its beautiful squares and that you may know, have
a curious system of roads: from each square a street to all other squares
that begin with a letter that is in its name (for example, from the Aro plaza
there are streets that lead to squares that begin with R, such as Plaza Ruido and Reto, or
by O, like Plaza Osa, but there are no streets to squares like Duende, Cascada or Tiara).
The streets are one-way (from Plaza Aro you can go to Plaça Ruido, but not
upside down since it does not meet the rule of the letters; Obviously, other places like Aro and Osa
they are connected to each other in both directions). All these connections between the N squares
they are collected in a street map, represented by an adjacency matrix of size NxN;
thus, the value of Callejero [p, q] indicates whether one can go from plaza p to plaza q.

April 26 is approaching, the feast of San Isidoro de Sevilla (pattern of letters
and, coincidentally, of the computer scientists), and in the City Council of Abcland they have decided that
to celebrate it, they will reverse the direction of all the streets that connect their squares.
On that day you can not move from Aro to Noise, but you will be allowed to go from Noise to Aro;
Obviously, Aro and Osa will remain connected to each other.

To formally design a standard Divide and Expire algorithm that, considering the
street map of the city (represented by the adjacency matrix), get the new
valid for the day of San Isidoro de Sevilla, indicating the structures of
data that is used.
'''

import math

### FUNCTIONS ###

# We need a matrix power of two for this method to work
# We expand with 0 rows and cols
def adaptStreetMap(streetMap):
    exp = 1
    size = 0
    while size < len(streetMap):
        size = math.pow(2, exp)
        exp += 1
    
    diff = int(size - len(streetMap))
    zeroes = [0] * diff # extra zeroes
    for street in streetMap:
        street.extend(zeroes)
    
    zeroes = [0] * len(streetMap[0]) # extra zeroes rows
    for i in range(diff):
        streetMap.append(zeroes)

# recover original size
def recoverStreetMap(streetMap, size_original):
    diff = int(len(streetMap) - size_original)
    for street in streetMap:
        # delete remaining cols
        del street[len(street) - diff:]

   # delete remaining rows
    del streetMap[len(streetMap) - diff:]

# Divide in four and traspose until 2x2
def invertirCallejero(c, iini, jini, ifin, jfin):
    if ifin - iini < 2:
        # 2x2, manual B / C exchange
        aux = c[iini][jfin]
        c[iini][jfin] = c[ifin][jini]
        c[ifin][jini] = aux
        return
    else:
        # 4 fours [A, B, C, D]
        imit = (ifin + iini) // 2
        jmit = (jfin + jini) // 2
        
        # traspose each one
        invertirCallejero(c, iini, jini, imit, jmit)          #A
        invertirCallejero(c, iini, jmit + 1, imit, jfin)      #B
        invertirCallejero(c, imit + 1, jini, ifin, jmit)      #C
        invertirCallejero(c, imit + 1, jmit + 1, ifin, jfin)  #D

        # exchange B/C
        baux = [] # BACKUP B AS VECTOR
        for i in range(iini, imit + 1):
            for j in range(jmit + 1, jfin + 1):
                baux.append(c[i][j])

        caux = [] # BACKUP C AS VECTOR
        index = 0
        for i in range(imit + 1, ifin + 1):
            for j in range(jini, jmit + 1):  
                caux.append(c[i][j])
                c[i][j] = baux[index]  # change: C <- B
                index += 1

        index = 0
        for i in range(iini, imit + 1):
            for j in range(jmit + 1, jfin + 1):
                c[i][j] = caux[index]  # change: B <- C
                index += 1

        return


### MAIN ###

# STREETMAP
# =========
############## Aro,     Ruido,   Reto,    Osa,     Duende,  Cascada, Tiara
########## Aro  1        1        1        1        0        0        0   
######## Ruido  0        1        1        1        1        0        0
######### Reto  0        1        1        1        0        0        1
########## Osa  1        0        0        1        0        0        0
####### Duende  0        0        0        0        1        0        0
###### Cascada  1        0        0        0        1        1        0
######## Tiara  1        1        1        0        0        0        1
streetMap = [
    [1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 1]
]

print('STREET MAP')
for street in streetMap:
    print(street)

size_original = len(streetMap)
adaptStreetMap(streetMap)
invertirCallejero(streetMap, 0, 0, len(streetMap)-1, len(streetMap)-1)
recoverStreetMap(streetMap, size_original)

print('26 APRIL')
for street in streetMap:
    print(street)
