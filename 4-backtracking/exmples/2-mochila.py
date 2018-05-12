objetos_pesos = [1, 2,  5,  6,  7]
objetos_valor = [1, 6, 18, 22, 28]

num_objetos = len(objetos_pesos)
mochila_capacidad = 11

solucion = [-1 for i in range(num_objetos)]
mochila_final = None
peso_final = 0
valor_final = 0

def mochila(solucion, k):
    global num_objetos
    i = 0
    while solucion[k] != 1: # for 0/1 (?)
        # primero es indefinido[-1], luego no se añade[0] y finalmente se añade[1] -> fin de while
        solucion[k] = i
        if valido(solucion):
            if k == num_objetos - 1:
                # ya hemos llegado a recorrer todos los objetos
                escribir(solucion)
            else:
                mochila(solucion, k+1)
        i += 1
    #volvemos a igualar la solución a -1
    solucion[k] = -1

def valido(solucion):
    global num_objetos, objetos_pesos, mochila_capacidad
    peso_aux = 0
    for i in range(num_objetos):
        if solucion[i] == 1:
            peso_aux += objetos_pesos[i]

    # es valido si no supera la capacidad de la mochila
    return mochila_capacidad >= peso_aux

def escribir(solucion):
    global valor_final, peso_final, mochila_final, num_objetos, objetos_pesos, objetos_valor
    peso_aux = 0
    valor_aux = 0
    for i in range(num_objetos):
        if solucion[i] == 1:
            peso_aux += objetos_pesos[i]
            valor_aux += objetos_valor[i]
    
    if valor_aux > valor_final:
        mochila_final = solucion[:]
        peso_final = peso_aux
        valor_final = valor_aux
            

mochila(solucion, 0)
print('EL VALOR DE LA MOCHILA ES', valor_final)
