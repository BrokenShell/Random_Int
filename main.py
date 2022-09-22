from Random_Int import random_int
from random import randint
from MonkeyScope import timer
from numpy.random import randint as np_randint


print("\nNaive Baseline\nrandom.randint")
timer(randint, 1, 10)

print("\nBaseline 2\nnumpy.random.randint")
timer(np_randint, 1, 10)

print("\nOur Custom Code\nRandom_Int.random_int")
timer(random_int, 1, 10)
