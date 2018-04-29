# Se tiene que almacenar un conjunto de n ficheros en una cinta magnética (soporte de 
# almacenamiento de recorrido secuencial), teniendo cada fichero una longitud conocida 
# l1, l2, ..., ln. Para simplificar el problema, puede suponerse que la velocidad de 
# lectura es constante, así como la densidad de información en la cinta.
# Se conoce de antemano la tasa de utilización de cada fichero almacenado, es decir, 
# se sabe la cantidad de peticiones pi correspondiente al fichero i que se van a realizar. 
# Por tanto, el total de peticiones al soporte será la cantidad  P = ∑ pi. Tras 
# la petición de un fichero, al ser encontrado la cinta es automáticamente rebobinada 
# hasta el comienzo de la misma.

# El objetivo es decidir el orden en que los n ficheros deben ser almacenados para que se 
# minimice el tiempo medio de carga, creando un algoritmo voraz correcto.

### FUNCTIONS ###

# FUNCION QUE ORDENA LA CINTA TENIENDO EN CUENTA DURACION Y NUMERO DE LECTURAS
def ordenarCinta(cinta, lecturas_cinta):
    cinta_ordenada = []
    while len(cinta) != 0:
        # TAMBIEN SE PODRÍA ORDENAR EN BASE A LA RELACIÓN CON QUICKSORT, SERÍA MÁS EFICIENTE
        mejor = 0
        for i in range(1, len(cinta)):
            if cinta[i]/lecturas_cinta[i] < cinta[mejor]/lecturas_cinta[mejor]:
                # FUNCION OBJETIVO
                mejor = i

        cinta_ordenada.append(cinta[mejor])
        del cinta[mejor]
    
    return cinta_ordenada


### MAIN ###
cinta = [10, 4, 2, 5, 9]
lecturas_cinta = [1, 3, 2, 9, 5]
orden_cinta = ordenarCinta(cinta, lecturas_cinta)

print('EL ORDEN DE LOS FICHEROS EN LA CINTA ES', orden_cinta)
