'''
After passing through the Tiles Room and getting the Cradle of Life, now Indiana
Croft faces a new challenge before being able to leave the Temple Cursed. It's found
on a bridge under which there is deep darkness. Fortunately, this place
It also appears in the diary. The bridge crosses the so-called Valley of Shadows, which begins
with a descent slope (the slope is not necessarily constant) for later
to reach the lowest point start to climb to the other end of the bridge (again,
not necessarily with constant slope). Right at the bottom of the valley there is a river,
but the newspaper does not specify its location with respect to the bridge (for example, you do not know
if the river is 53 meters from the beginning of the bridge) or the distance in height (it is
say, it is not known if the river is 228 meters below, for example). On the slopes
there are sharp rocks.

If Indiana Croft had time, he could easily find the point where
get off the bridge to get exactly to the river, as it has a laser pointer
to measure heights that tells you how many meters there are from the bridge to the ground at a point
determined. The problem is that the priests of the temple have found out that they have been robbed
the Cradle of Life, they are chasing Indiana Croft and they will reach you right away. He
Adventurer must quickly find the position of the river to get off and flee safely.

Design the algorithm that Indiana Croft should use to find the valley's minimum point
in the indicated conditions. The algorithm must be efficient: at least in the best case
it must have a logarithmic order. You can consider how long Indiana Croft takes in
move along the bridge is null and that the estimate of the point of the river where
Picking off can have an approximation error of E meters (E is a given constant).
'''

import math

### FUNCTIONS ###

# Function that returns the distance to the valley from a position of the bridge
def laserPointer(x):
    return math.pow(x, 2) - 10

# Recursive function that receives the bridge interval[p] and the error[e]
# and returns an interval that contains the x so LASERPOINTER(X)=MIN with the error < e
def lookForRiver(p, e):
    laserPointer_p0 = laserPointer(p[0])
    # laserPointer_p1 = laserPointer(p[1])
    
    if abs(p[1] - p[0]) < e:
        # Valid interval
        return p
    else:
        # divide by 3 and check in which is definitely not minimum
        oneThird = p[0] + (p[1] - p[0]) * (1/3)
        twoThirds = p[0] + (p[1] - p[0]) * (2/3)
        laserPointer_oneThird = laserPointer(oneThird)
        laserPointer_twoThirds = laserPointer(twoThirds)

        # if 1/3 decreases and 2/3 decreases we can discard the first part,
        # if 2/3 increases we can discard the last
        if laserPointer_p0 > laserPointer_oneThird > laserPointer_twoThirds:
            interval = [oneThird, p[1]]
        else:
            interval = [p[0], twoThirds]

        return lookForRiver(interval, e)

### MAIN ###
bridge = [-2, 3]
err = 0.05

resultado = lookForRiver(bridge, err)
print('The bridge starts in', bridge[0], 'and ends in', bridge[1], 'the river is in', resultado)
