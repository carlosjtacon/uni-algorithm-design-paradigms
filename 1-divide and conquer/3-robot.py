'''
We need to program a robot to put caps in bottles. We have N bottles and N caps,
but a series of problems:

- Bottles are unique, so do caps. Only one specific cap can match with a bottle.
- The only thing the robot can do is compare bottles and caps. It can detect if a 
cap is smaller, bigger or equal.
- Robot cannot order caps nor bottles.
- Robot can distribute caps and bottles in different positions of the table.
'''

### FUNCTIONS ###
# When it fit, removes from list and fit list-1 
def fit(result, caps, bottles):
    if len(caps) == 1:
        result.append([caps[0], bottles[0]])
        return
    cap = caps[0]
    for bottle in bottles:
        if cap == bottle:
            caps.remove(cap)
            bottles.remove(bottle)
            result.append([cap, bottle])
            fit(result, caps, bottles)
            return

# Improved version that organise the list with one pivot
def improvedFit(result, caps, bottles):
    if len(caps) == 1:
        result.append([caps[0], bottles[0]])
        return
    
    cap = caps[0]
    bottle_pivot = []
    bottles_lessthan_pivot = []
    bottles_greaterthan_pivot = []
    for bottle in bottles:
        if cap > bottle:
            bottles_lessthan_pivot.append(bottle)
        elif cap < bottle:
            bottles_greaterthan_pivot.append(bottle)
        elif cap == bottle:
            bottle_pivot.append(bottle)
            result.append([cap, bottle])
    
    caps.remove(cap)
    bottle_pivot.append(len(bottles_lessthan_pivot)) # pivot index into organised vector will be number of lower bottles
    organised_bottles = bottles_lessthan_pivot[:]
    organised_bottles.append(bottle_pivot[0])
    organised_bottles.extend(bottles_greaterthan_pivot)
    fitPivot(result, caps, organised_bottles, bottle_pivot)
    return

# Function that fits cap with bottle having a pivot([0]=value, [1]=index)
# ald going left or right of pivot
def fitPivot(result, caps, bottles, bottle_pivot):
    if len(caps) == 1:
        return

    cap = caps[0]
    if cap > bottle_pivot[0]:
        for bottle in bottles[bottle_pivot[1]:]:
            # loop from pivot to end
            if cap == bottle:
                caps.remove(cap)
                bottles.remove(bottle)
                result.append([cap, bottle])
                fitPivot(result, caps, bottles, bottle_pivot)
                return
    else:
        for bottle in bottles[:bottle_pivot[1]]:
            # loop from init to pivot
            if cap == bottle:
                caps.remove(cap)
                bottles.remove(bottle)
                result.append([cap, bottle])
                bottle_pivot[1] -= 1 # decrease pivot index because we removed an element
                fitPivot(result, caps, bottles, bottle_pivot)
                return

### MAIN ###
caps  = [2, 4, 6, 8, 1, 3, 5, 7, 9]
bottles = [1, 3, 5, 7, 9, 2, 4, 6, 8]

fit_result = []
# fit(fit_result, caps, bottles)
improvedFit(fit_result, caps, bottles)
print('RESULT', fit_result)
