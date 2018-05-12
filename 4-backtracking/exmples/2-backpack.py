obj_weight = [1, 2,  5,  6,  7]
obj_values = [1, 6, 18, 22, 28]

num_obj = len(obj_weight)
backpack_capacity = 11

solution = [-1 for i in range(num_obj)]
backpack_end = None
weight_end = 0
value_end = 0

def backpack(solution, k):
    global num_obj
    i = 0
    while solution[k] != 1:
        solution[k] = i
        if valid(solution):
            if k == num_obj - 1:
                escribir(solution)
            else:
                backpack(solution, k+1)
        i += 1
    solution[k] = -1

def valid(solution):
    global num_obj, obj_weight, backpack_capacity
    weight_aux = 0
    for i in range(num_obj):
        if solution[i] == 1:
            weight_aux += obj_weight[i]

    return backpack_capacity >= weight_aux

def escribir(solution):
    global value_end, weight_end, backpack_end, num_obj, obj_weight, obj_values
    weight_aux = 0
    valor_aux = 0
    for i in range(num_obj):
        if solution[i] == 1:
            weight_aux += obj_weight[i]
            valor_aux += obj_values[i]
    
    if valor_aux > value_end:
        backpack_end = solution[:]
        weight_end = weight_aux
        value_end = valor_aux
            

backpack(solution, 0)
print('backpack value', value_end)
