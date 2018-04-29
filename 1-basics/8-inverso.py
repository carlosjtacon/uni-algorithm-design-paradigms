# Realizar un procedimiento recursivo que calcule el número inverso de uno dado. 
# Ejemplo : 627 -> 726
# Realiza un análisis de eficiencia y de complejidad.

import math

### FUNCTIONS ###
def calculaInversoRecursivo(num):
    escala = int(math.log10(num))
    valor = num // 10
    resto = num % 10
    if valor == 0:
        return resto
    else:
        return resto * (10 ** escala) + calculaInversoRecursivo(valor)


### MAIN ###
numero = int(input('NÚMERO:\n'))
inversoRecursivo = calculaInversoRecursivo(numero)
print('INVERSO RECURSIVO', inversoRecursivo)