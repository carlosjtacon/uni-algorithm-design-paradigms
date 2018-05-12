'''
We have a function f(x) in which the interval [p1, p2] has a unique minimum at x0, decreasing 
between [p1, x0] and increasing between [x0, p2]. Note: x0 may be p1 or p2.

Search as efficient as possible each point x in [p1, p2] in which f(x) returns a k value, so
{x ∈ [p1, p2] that f(x) = k}.

In order to simplify, instead of calculating the exact x value we can calculate an interval
with error, [α, β] and β – α < ε.
'''

### FUNCTIONS ###
# Function with minimum (0)
def f(x):
    return x ** 2

# Recursive function with parameters: interval[p], error[e] value[k]
# returning 1 or 2 intervals that cointains the [x] so f(x)=k with error < [e]
def searchValues(p, e, k):
    f_p0 = f(p[0])
    f_p1 = f(p[1])

    # 3 Possibilities:
    #     - F(p0) > K && F(p1) > K: 2 Cuts / None
    #     - F(p0) < K && F(p1) < K: None
    #     - Else: 1 Cut
    if f_p0 < k > f_p1:
        # 2 Cuts below k,
        # Interval dont exist
        return None
    elif f_p0 > k < f_p1:
        # 2 Cuts above k,
        # 2 left / 2 right / 1 left + 1 right from k
        oneThird = p[0] + (p[1] - p[0]) * (1 / 3)
        twoThirds = p[0] + (p[1] - p[0]) * (2 / 3)
        f_oneThird = f(oneThird)
        f_twoThirds = f(twoThirds)

        result, val1, val2 = [], [], []
        if f_oneThird < k > f_twoThirds:
            # Values lower than k, we delete the center piece
            val1 = searchOneValue([p[0], oneThird], e, k)
            val2 = searchOneValue([twoThirds, p[1]], e, k)
        elif f_oneThird > k > f_twoThirds:
            # k between divisions
            val1 = searchOneValue([oneThird, twoThirds], e, k)
            val2 = searchOneValue([twoThirds, p[1]], e, k)
        elif f_oneThird < k < f_twoThirds:
            # k between divisions
            val1 = searchOneValue([p[0], oneThird], e, k)
            val2 = searchOneValue([oneThird, twoThirds], e, k)
        else: 
            # 2 left / 2 right / 1 left + 1 right from k
            if f_p0 > f_oneThird > f_twoThirds:
                return searchValues([oneThird, p[1]], e, k)
            else:
                return searchValues([p[0], twoThirds], e, k)

        result.append(val1)
        result.append(val2)
        return result
    else:
        # One point above and one below, just one cut
        return searchOneValue(p, e, k)


# Recursive function with parameters: interval[p], error[e] value[k]
# returning 1 interval that cointains the [x] so f(x)=k with error < [e]
def searchOneValue(p, e, k):
    f_p0 = f(p[0])
    # f_p1 = f(p[1])

    if abs(p[1] - p[0]) < e:
        # Valid interval
        return p
    else:
        mid = p[0] + (p[1] - p[0]) / 2
        f_mitad = f(mid)
        # knowing f(mid) we can discard one value
        if f_p0 <= k <= f_mitad or f_p0 >= k >= f_mitad:
            return searchOneValue([p[0], mid], e, k)
        else:
            return searchOneValue([mid, p[1]], e, k)


### MAIN ###
# interval = [-2, 0]
# interval = [0, 2]
interval = [-50, 200]
error = 0.05
value = 3.0625 #f(1.75)

result = searchValues(interval, error, value)
print('F(X) =', value,'in the intervals', result)
