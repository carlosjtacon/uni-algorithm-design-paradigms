'''
Shrek, Donkey and Dragona arrive at the foot of Lord Farquaad's towering castle.
free Fiona from her confinement. As they suspected that the drawbridge would be guarded
many soldiers have brought many ladders, of different heights, with the hope
that some of them allow them to overcome the wall; but no stairs serve them
because the wall is very high. Shrek realizes that, if he could combine all the
stairs in one, would get exactly to the top and be able to enter
to the castle.
Fortunately the stairs are made of iron, so with the help of Dragona they go to
"Solder them". Dragona can weld any two stairs with her fire breath,
but it takes to heat the ends as many minutes as meters add up the stairs to be welded.
For example, welding 6 and 8 meters of stairs would take 6 + 8 = 14 minutes. If to this
ladder was welded after a 7-meter, the new time would be 14 + 7 = 21 minutes,
so it would have taken to make the whole ladder a total of 14 + 21 = 35 minutes.
Design an efficient algorithm that finds the best cost and way to weld the stairs
to make Shrek as late as possible is to climb the wall, indicating the structures of
chosen data and its form of use. It can be assumed that exactly the
necessary stairs to climb the wall (there is no need or lack), that is, the data
of the problem is the collection of measures of the "miniescaleras" (in the data structure
that is chosen), and that only the optimal way of melting the stairs is looked for.
'''

### FUNCTIONS ###

def joinStairs(stairs):
    total = 0
    ordered_stairs = []
    while len(stairs) != 0:
        best = 0
        for i in range(1, len(stairs)):
            if stairs[i] < stairs[best]:
                best = i

        total += total + stairs[best]
        ordered_stairs.append(stairs[best])
        del stairs[best]

    print('SELECTION', ordered_stairs)
    return total


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

# better with quicksort
def joinStairsQuick(stairs):
    total = 0
    ordered_stairs = quicksort(stairs)
    for i in range(0, len(ordered_stairs)):
        total += total + ordered_stairs[i]

    print('QUICKSORT', ordered_stairs)
    return total


### MAIN ###
stairs = [10, 4, 2, 5, 9]
total = joinStairs(stairs)
# total = joinStairsQuick(stairs)

print('Total time', total)
