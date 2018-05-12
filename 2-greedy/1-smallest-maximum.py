'''
We have n natural numbers, n being an even number, which have to come together forming
pairs of two numbers each. Then, from each pair you get the sum of your
two components, and of all these results the maximum is taken.

Design a greedy algorithm that creates the pairs so that the maximum value of the sums
of the numbers of each pair is as small as possible, demonstrating that the function of
Selection of candidates used provides an optimal solution.

Example: assuming that the data is in the following vector [5,8,1,4,7,9]
Let's see a couple of ways to solve the problem (not necessarily the optimal one):
We select as a couple the consecutive elements
In this way we get the pairs (5, 8), (1, 4) and (7, 9); so,
when adding the components we have the values 15, 5 and 16, so the result
final is 16. We select as a pair the opposite elements in the vector
Now we have the pairs (5, 9), (8, 7) and (1, 4); adding we get 14, 15 and 5, for
what the final result is 15 (better than before).
Will there be a better result for this problem? Can a method be generalized that
provide a correct voracious algorithm for any amount of data, and that
be independent of the value of them?
'''

### FUNCTIONS ###
def quicksort(vector):
    if len(vector) == 1 or len(vector) == 0:
        return vector
    else:
        pivot = vector[0]
        i = 0
        for j in range(len(vector) - 1):
            if vector[j + 1] < pivot:
                vector[j + 1], vector[i + 1] = vector[i + 1], vector[j + 1]
                i += 1
        vector[0], vector[i] = vector[i], vector[0]
        first_part = quicksort(vector[:i])
        second_part = quicksort(vector[i + 1:])
        first_part.append(vector[i])
        return first_part + second_part

# Returns the smallest maximum of pairs on the array
# We need to combine vector[0] with vector[n], [1] with [n-1]...
def pair(vector):

    print('VECTOR', vector)
    vector = quicksort(vector)
    print('SORTED', vector)

    maximum = -1
    for i in range(0, len(vector) // 2):
        _pair = vector[i] + vector[len(vector) - 1 - i]
        print('PAIR', vector[i], vector[len(vector) - 1 - i], '=', _pair)
        if _pair > maximum:
            maximum = _pair
        
    return maximum

### MAIN ###
vector = [5, 8, 1, 4, 7, 9]
smallest_max = pair(vector)

print('SMALLEST MAX', smallest_max)
