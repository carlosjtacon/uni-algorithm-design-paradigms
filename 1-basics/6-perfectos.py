# Realiza el pseudocódigo de una función que determine si un número recibido 
# como parámetro es perfecto. Realiza un análisis de eficiencia y de complejidad.

### FUNCTIONS ###

# UN NUMERO ES PERFECTO SI LA SUMA
# DE SUS DIVISORES ES IGUAL AL NUMERO
def esPerfecto(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i

    return num == suma_divisores


### MAIN ###
numero = int(input('NÚMERO:\n'))
perfecto = esPerfecto(numero)
if perfecto:
    print('ES PERFECTO')
else:
    print('NO ES PERFECTO')
