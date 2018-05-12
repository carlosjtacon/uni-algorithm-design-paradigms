'''
A set of n files must be stored on a magnetic tape (support for
sequential travel storage), each file having a known length
l1, l2, ..., ln. To simplify the problem, it can be assumed that the speed of
reading is constant, as well as the information density on the tape.
It is known in advance the rate of use of each stored file, that is,
we know the number of pi requests corresponding to the file i that will be made.
Therefore, the total requests to the support will be the amount P = Σ pi. After
the request of a file, when the tape is found is automatically rewound
until the beginning of it.

The objective is to decide the order in which the n files should be stored so that
Minimize the average loading time, creating a correct greedy algorithm.
'''

### FUNCTIONS ###

# Order tape by length and number of reads
def orderTape(tape, reads_tape):
    tape_ordered = []
    while len(tape) != 0:
        # we could also use quicksort
        best = 0
        for i in range(1, len(tape)):
            if tape[i]/reads_tape[i] < tape[best]/reads_tape[best]:
                best = i

        tape_ordered.append(tape[best])
        del tape[best]
    
    return tape_ordered


### MAIN ###
tape = [10, 4, 2, 5, 9]
reads_tape = [1, 3, 2, 9, 5]
orden_tape = orderTape(tape, reads_tape)

print('Correct order', orden_tape)
