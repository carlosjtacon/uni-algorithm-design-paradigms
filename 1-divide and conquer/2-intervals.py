'''
Se tiene acceso a una función f(x) de la que se sabe que en el intervalo real 
[p1, p2] tiene un único mínimo local en el punto x0, que es estrictamente decreciente
entre [p1, x0] y que es estrictamente creciente entre [x0, p2]. Hay que observar 
que x0 puede coincidir con p1 o con p2.
Se tiene que buscar, de la manera más eficiente posible, todos los puntos x 
(si es que existen) del intervalo [p1, p2] tales que la función f tome un cierto 
valor k, es decir, se busca el conjunto de valores {x ∈ [p1, p2] tal que f(x) = k}. 
Para simplificar el proceso, en vez del valor exacto de cada x puede indicarse un 
intervalo de valores [α, β], con β – α < ε, donde se encuentre x. Los datos del 
algoritmo serán el intervalo [p1, p2], el valor k que se está buscando, y el valor 
ε para la aproximación.
'''

### FUNCTIONS ###

# FUNCIÓN POLINÓMICA CON UN MÍNIMO
def f(x):
    return x ** 2

# FUNCIÓN RECURSIVA QUE RECIBE UN INTERVALO[p], UNA APROXIMACIÓN[e] Y UN VALOR[k]
# QUE DEVUELVE UNO O DOS INTERVALOS QUE CONTIENEN LA X PARA QUE F(X)=K
# CON UN ERROR MENOR AL VALOR DE LA APROXIMACIÓN
def buscarValores(p, e, k):
    f_p0 = f(p[0])
    f_p1 = f(p[1])

    # TENEMOS TRES POSIBILIDADES:
    #     - F(p0) > K && F(p1) > K: PUEDE TENER 2 CORTES O NONE
    #     - F(p0) < K && F(p1) < K: NONE
    #     - ELSE: 1 CORTE
    if f_p0 < k > f_p1:
        # LOS DOS CORTES ESTÁN POR DEBAJO DE K,
        # ASÍ QUE NO SE ENCUENTRA EN EL INTERVALO
        return None
    elif f_p0 > k < f_p1:
        # LOS DOS CORTES ESTÁN POR ENCIMA DE K,
        # PUEDEN ESTAR LOS DOS A LA IZQUIERDA DE K,
        # LOS DOS A LA DERECHA O UNO EN CADA LADO
        unTercio = p[0] + (p[1] - p[0]) * (1 / 3)
        dosTercios = p[0] + (p[1] - p[0]) * (2 / 3)
        f_unTercio = f(unTercio)
        f_dosTercios = f(dosTercios)

        resultado, val1, val2 = [], [], []
        if f_unTercio < k > f_dosTercios:
            # LOS DOS VALORES SON MENORES A K, ELIMINAMOS EL TROZO CENTRAL
            val1 = buscarUnValor([p[0], unTercio], e, k)
            val2 = buscarUnValor([dosTercios, p[1]], e, k)
        elif f_unTercio > k > f_dosTercios:
            # EL VALOR K ESTÁ ENTRE LAS DIVISIONES
            val1 = buscarUnValor([unTercio, dosTercios], e, k)
            val2 = buscarUnValor([dosTercios, p[1]], e, k)
        elif f_unTercio < k < f_dosTercios:
            # EL VALOR K ESTÁ ENTRE LAS DIVISIONES
            val1 = buscarUnValor([p[0], unTercio], e, k)
            val2 = buscarUnValor([unTercio, dosTercios], e, k)
        else: 
            # PUEDE SER LOS DOS MAYORES POR LA IZQUIERDA,
            # LOS DOS POR LA DERECHA O UNO POR CADA LADO
            if f_p0 > f_unTercio > f_dosTercios:
                return buscarValores([unTercio, p[1]], e, k)
            else:
                return buscarValores([p[0], dosTercios], e, k)

        resultado.append(val1)
        resultado.append(val2)
        return resultado
    else:
        # UN PUNTO POR ARRIBA Y UNO POR ABAJO,
        # ASÍ QUE SOLO HAY UN CORTE
        return buscarUnValor(p, e, k)


# FUNCIÓN RECURSIVA QUE RECIBE UN INTERVALO[p], UNA APROXIMACIÓN[e] Y UN VALOR[k] 
# ENTRE F(p0) Y F(p1) QUE DEVUELVE UN INTERVALO QUE CONTIENE LA X PARA QUE F(X)=K
# CON UN ERROR MENOR AL VALOR DE LA APROXIMACIÓN
def buscarUnValor(p, e, k):
    f_p0 = f(p[0])
    f_p1 = f(p[1])
    
    # print('p[0]', p[0], 'p[1]', p[1])
    # print('f(p[0]) =', f_p0, '| f(p[1]) =', f_p1)
    # (???) if abs(abs(k) - abs(f_p0)) < e and abs(abs(f_p1) - abs(k)) < e:
    
    if abs(p[1] - p[0]) < e:
        # ENTONCES EL INTERVALO ES 
        # VÁLIDO Y LO DEVOLVEMOS
        return p
    else:
        mitad = p[0] + (p[1] - p[0]) / 2
        f_mitad = f(mitad)
        # SABIENDO EL F(MITAD) PODEMOS DESCARTAR EL INTERVALO QUE NO INCLUYA K
        # PUEDE SER QUE ESTA PARTE DE F(X) ESTÉ BAJANDO O SUBIENDO, HAY QUE TENER AMBAS EN CUENTA
        if f_p0 <= k <= f_mitad or f_p0 >= k >= f_mitad:
            return buscarUnValor([p[0], mitad], e, k)
        else:
            return buscarUnValor([mitad, p[1]], e, k)


### MAIN ###
# intervalo = [-2, 0]
# intervalo = [0, 2]
intervalo = [-50, 200]
aprox = 0.05
valor = 3.0625 #f(1.75)

resultado = buscarValores(intervalo, aprox, valor)
print('F(X) =', valor,'PARA X EN ESTOS INTERVALOS', resultado)
