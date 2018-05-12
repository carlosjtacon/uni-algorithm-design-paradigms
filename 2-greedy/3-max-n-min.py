'''
There is a vector V formed by n data, from which you want to find the
minimal vector element and maximum vector element. The type of the data
what's in the vector is not relevant to the problem, but the comparison between
two data to see which is less is very expensive, so the algorithm for the
search for the minimum and maximum should make the least amount of comparisons between
possible elements.

A trivial method consists of a linear path of the vector to search for the maximum and
then another tour to look for the minimum, which requires a total of approximately
2n comparisons between data. This method is not fast enough, so it is
asks to implement a method with greedy methodology that makes a maximum of 3/2n comparisons.
'''

### FUNCTIONS ###
def getGreater(a, b):
    return a if a > b else b

def maxMin(vector):
    print('VECTOR', vector)
    i = 0
    vectorMinimum = []
    vectorMaximum = []
    while i < len(vector):
        # two vectors, one of the ones that have been greater and the rest
        # we can assure that in the first one will be the max and the min in the other
        
        if i == len(vector) -1:
            # last odd position, with previous
            if vector[i] > vector[i - 1]:
                vectorMaximum.append(vector[i])
            else:
                vectorMinimum.append(vector[i])
        elif vector[i] > vector[i + 1]:
            vectorMaximum.append(vector[i])
            vectorMinimum.append(vector[i + 1])
        else:
            vectorMaximum.append(vector[i + 1])
            vectorMinimum.append(vector[i])
        
        # increase by 2 so loop only N/2
        i += 2
    
    print('VECTOR Minimum', vectorMinimum)
    print('VECTOR Maximum', vectorMaximum)

    Minimum = vectorMinimum[0]
    for k in range(1, len(vectorMinimum)):
        # find min N/2
        if vectorMinimum[k] < Minimum:
            Minimum = vectorMinimum[k]

    Maximum = vectorMaximum[0]
    for j in range(1, len(vectorMaximum)):
        # find max N/2
        if vectorMaximum[j] > Maximum:
            Maximum = vectorMaximum[j]

    return [Minimum, Maximum]


### MAIN ###
v = [10, 4, 5, 11, 1, -1, 23]
result = maxMin(v)
print('min', result[0], 'amd max', result[1])
