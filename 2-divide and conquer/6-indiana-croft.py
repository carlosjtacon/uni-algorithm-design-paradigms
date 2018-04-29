# Tras su paso por la Sala de las Baldosas y conseguir la Cuna de la Vida, ahora Indiana 
# Croft se enfrenta a un nuevo desafío antes de poder salir del Templo Maldito. Se encuentra 
# en un puente bajo el que se observa una profunda oscuridad. Afortunadamente, este lugar 
# también aparece en el diario. El puente cruza el llamado Valle de Sombras, que empieza 
# con una pendiente de bajada (la pendiente no es necesariamente constante) para después 
# de llegar al punto más bajo empezar a subir hasta el otro extremo del puente (de nuevo, 
# no necesariamente con pendiente contante). Justo en la parte inferior del valle hay un río, 
# pero el diario no especifica su ubicación con respecto al puente (por ejemplo, no se sabe 
# si el río está a 53 metros desde el comienzo del puente) ni la distancia en altura (es 
# decir, no se sabe si el río está 228 metros por debajo, por ejemplo). En las pendientes 
# hay afiladísimas rocas.

# Si Indiana Croft tuviese tiempo, podría encontrar sin problema el punto por donde 
# descolgarse del puente para llegar exactamente al río, ya que tiene un puntero laser 
# para medir alturas que le dice cuántos metros hay desde el puente hasta el suelo en un punto 
# determinado. El problema es que los sacerdotes del templo han averiguado que les han robado 
# la Cuna de la Vida, están persiguiendo a Indiana Croft y le alcanzarán enseguida. El 
# aventurero debe encontrar rápidamente la posición del río para descolgarse y huir seguro.

# Diseñar el algoritmo que debería usar Indiana Croft para buscar el punto mínimo del valle 
# en las condiciones indicadas. El algoritmo debe ser eficiente: al menos en el mejor caso 
# debe tener un orden logarítmico. Se puede considerar el tiempo que tarda Indiana Croft en 
# desplazarse a lo largo del puente es nulo y que la estimación del punto del río por donde 
# descolgarse puede tener un error de aproximación de  metros ( es una constante dada).

import math

### FUNCTIONS ###

# FUNCIÓN QUE DEVUELVE EL VALOR DE LA FUNCIÓN 
# DEL VALLE PARA UNA POSICIÓN DEL PUENTE
def punteroLaser(x):
    return math.pow(x, 2) - 10

# FUNCIÓN RECURSIVA QUE RECIBE EL INICIO Y FIN DEL PUENTE - UN INTERVALO[p] -, UNA APROXIMACIÓN[e]
# Y QUE DEVUELVE UN INTERVALO QUE CONTIENE LA X PARA QUE PUNTEROLASER(X)=MINIMO 
# CON UN ERROR MENOR AL VALOR DE LA APROXIMACIÓN
def buscarRio(p, e):
    punteroLaser_p0 = punteroLaser(p[0])
    punteroLaser_p1 = punteroLaser(p[1])
    
    if abs(p[1] - p[0]) < e:
        # ENTONCES EL INTERVALO ES 
        # VÁLIDO Y LO DEVOLVEMOS
        return p
    else:
        # DIVIDIMOS EN TRES Y MIRAMOS EN CUAL NO ESTÁ EL MINIMO
        unTercio = p[0] + (p[1] - p[0]) * (1/3)
        dosTercios = p[0] + (p[1] - p[0]) * (2/3)
        punteroLaser_unTercio = punteroLaser(unTercio)
        punteroLaser_dosTercios = punteroLaser(dosTercios)

        # SABEMOS QUE SI BAJA EN 1/3 Y TAMBIÉN EN 2/3 
        # PODEMOS DESCARTAR EL PRIMER TRAMO DE INTERVALO,
        # SI EN 2/3 SUBE SABEMOS QUE PODEMOS DESCARTAR EL ÚLTIMO TRAMO
        if punteroLaser_p0 > punteroLaser_unTercio > punteroLaser_dosTercios:
            intervalo = [unTercio, p[1]]
        else:
            intervalo = [p[0], dosTercios]

        return buscarRio(intervalo, e)

### MAIN ###
puente = [-2, 3]
aprox = 0.05

resultado = buscarRio(puente, aprox)
print('EL PUENTE EMPIEZA EN', puente[0], 'Y TERMINA EN', puente[1], 'TENDRÁ QUE DESCOLGARSE EN EL INTERVALO', resultado)
