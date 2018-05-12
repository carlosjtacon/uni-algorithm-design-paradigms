# Se quiere programar un robot para poner tapones de corcho a las botellas 
# de una fábrica de reciclado. Se tienen disponibles N botellas y los N corchos 
# que las tapan (N es constante en el problema), pero hay una serie de problemas:

#  Las botellas son todas distintas entre sí, igual que los corchos: cada botella 
# solo puede cerrarse con un corcho concreto, y cada corcho solo sirve para una botella 
# concreta.
#  El robot está preparado para cerrar botellas, por lo que lo único que sabe hacer 
# es comparar corchos con botellas. El robot puede detectar si un corcho es demasiado 
# pequeño, demasiado grande, o del tamaño justo para cerrar una botella.
#  El robot no puede comparar corchos entre sí para “ordenarlos” por grosor, y tampoco 
# puede hacerlo con las botellas.
#  El robot tiene espacio disponible y brazos mecánicos para colocar botellas y corchos 
# a su antojo, por ejemplo en distintas posiciones de una mesa, si es necesario.

# Diseñar el algoritmo que necesita el robot para taponar las N botellas de manera óptima.

### FUNCTIONS ###

# ENCAJA TAPONES CON BOTELLAS, CUANDO ENCAJA 
# UNA LA QUITA DE LA LISTA Y ENCAJA LA LISTA - 1 
def encajar(resultado, tapones, botellas):
    if len(tapones) == 1:
        resultado.append([tapones[0], botellas[0]])
        return
    tapon = tapones[0]
    for botella in botellas:
        if tapon == botella:
            tapones.remove(tapon)
            botellas.remove(botella)
            resultado.append([tapon, botella])
            encajar(resultado, tapones, botellas)
            return

# VERSION MEJOR QUE ORGANIZA LA LISTA EN TORNO A UN PIVOTE
# POR MAYOR O MENOR ANTES DE ENCAJAR TAPON Y BOTELLA
def encajarMejorado(resultado, tapones, botellas):
    if len(tapones) == 1:
        resultado.append([tapones[0], botellas[0]])
        return
    
    tapon = tapones[0]
    botella_pivote = []
    botellas_menores_pivote = []
    botellas_mayores_pivote = []
    for botella in botellas:
        if tapon > botella:
            botellas_menores_pivote.append(botella)
        elif tapon < botella:
            botellas_mayores_pivote.append(botella)
        elif tapon == botella:
            botella_pivote.append(botella)
            resultado.append([tapon, botella])
    
    tapones.remove(tapon)
    botella_pivote.append(len(botellas_menores_pivote)) # EL INDICE PIVOTE EN EL VECTOR ORGANIZADO SERÁ EL NUMERO DE BOTELLAS MENORES
    botellas_organizadas = botellas_menores_pivote[:]
    botellas_organizadas.append(botella_pivote[0])
    botellas_organizadas.extend(botellas_mayores_pivote)
    encajarPivote(resultado, tapones, botellas_organizadas, botella_pivote)
    return

# FUNCION QUE ENCAJA EL TAPON CON LA BOTELLA TENIENDO EN CUENTA UNA BOTELLA 
# PIVOTE([0]=valor, [1]=indice), Y YENDO A IZQUIERDA O DERECHA DE ESTA
def encajarPivote(resultado, tapones, botellas, botella_pivote):
    if len(tapones) == 1:
        return

    tapon = tapones[0]
    if tapon > botella_pivote[0]:
        for botella in botellas[botella_pivote[1]:]:
            # RECORREMOS DESDE EL PIVOTE HASTA EL FINAL N/2
            if tapon == botella:
                tapones.remove(tapon)
                botellas.remove(botella)
                resultado.append([tapon, botella])
                encajarPivote(resultado, tapones, botellas, botella_pivote)
                return
    else:
        for botella in botellas[:botella_pivote[1]]:
            # RECORREMOS DESDE EL INICIO HASTA EL PIVOTE N/2
            if tapon == botella:
                tapones.remove(tapon)
                botellas.remove(botella)
                resultado.append([tapon, botella])
                botella_pivote[1] -= 1 # DECREMENTAMOS EL INDICE DEL PIVOTE YA QUE HEMOS ELIMINADO UN ELEMENTO A LA IZQUIERDA 
                encajarPivote(resultado, tapones, botellas, botella_pivote)
                return

### MAIN ###
tapones  = [2, 4, 6, 8, 1, 3, 5, 7, 9]
botellas = [1, 3, 5, 7, 9, 2, 4, 6, 8]

encajar_resultado = []
# encajar(encajar_resultado, tapones, botellas)
encajarMejorado(encajar_resultado, tapones, botellas)
print('RESULTADO', encajar_resultado)
