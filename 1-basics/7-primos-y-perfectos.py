# Realiza el pseudocódigo de un programa que pida un número 
# positivo al usuario (N) y le diga cuantos primos hay entre 1 y ese 
# número N, y cuantos perfectos hay entre 1 y ese número N. Realiza un
# análisis de eficiencia y de complejidad.

### FUNCTIONS ###
def esPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def esPerfecto(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i

    return num == suma_divisores


### MAIN ###
numero = int(input('NÚMERO:\n'))
primos, perfectos = 0, 0
for i in range(1, numero):
    if esPrimo(i):
        primos += 1
    if esPerfecto(i):
        perfectos += 1
print(primos, 'NUMEROS PRIMOS |', perfectos, 'NUMEROS PERFECTOS')
