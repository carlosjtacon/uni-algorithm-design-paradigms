# Realiza el pseudocódigo de una función que determine si un número 
# recibido como parámetro es primo. Realiza un análisis de eficiencia y de complejidad.

### FUNCTIONS ###

# UN NUMERO ES PRIMO SI SOLO ES DIVISIBLE 
# POR ÉL MISMO Y LA UNIDAD
def esPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


### MAIN ###
numero = int(input('NÚMERO:\n'))
primo = esPrimo(numero)
if primo:
    print('ES PRIMO')
else:
    print('NO ES PRIMO')
