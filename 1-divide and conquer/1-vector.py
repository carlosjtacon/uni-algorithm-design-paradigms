'''
We have a vector V[1..N] containing unique integers, and ordered from lowest to highest. 
This vector is coincident if it has at least one position equal to its value. 
E.g. [-14,-6,3,6,16,28,37,43], V[3] = 3; so this vector is coincident.

Algorithm with efficiency less or equal than O(log N) that checks if coincident.
'''

### FUNCTIONS ###
# Using init[xi] position and end[xe], order required to discard
def isCoincident(xi, xe, v):
    coincident = False
    if xi == xe:
        if v[xi] == xi:
            coincident = True
    else:
        mid = (xi + xe) // 2
        if v[mid] == mid:
            coincident = True
        else:
            # Since it is ordered and not coincident in the mid position, there is 
            # one posibility of coincident: left or right part.
            if v[mid] < mid:
                xi = mid + 1
            else:
                xe = mid - 1
            coincident = isCoincident(xi, xe, v)
    
    return coincident

### MAIN ###
# vector = [-14, -6, 3, 6, 16, 18, 27, 43]      # NO COINCIDENT
vector = [-20, -14, -6, 3, 6, 16, 18, 27, 43]   # COINCIDENT (3)

is_coincident = isCoincident(0, len(vector) - 1, vector)
print('COINCIDENT' if is_coincident else 'NO COINCIDENT', vector)