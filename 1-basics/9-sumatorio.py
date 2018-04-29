# Realizar una función recursiva que calcule el siguiente sumatorio: S= 1+2+3+4+....+n-1+n.
# Realiza un análisis de eficiencia y de complejidad.

### FUNCTIONS ###
def calculaSumatorio(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

def calculaSumatorioRecursivo(num):
    if num == 1:
        return 1
    else:
        return num + calculaSumatorioRecursivo(num - 1)


### MAIN ###
numero = int(input('NÚMERO:\n'))
sumatorio = calculaSumatorio(numero)
sumatorioRecursivo = calculaSumatorioRecursivo(numero)
print('SUMATORIO', sumatorio)
print('SUMATORIO RECURSIVO', sumatorioRecursivo)