from Random_Int import random_int
from random import randint
from MonkeyScope import distribution_timer
from numpy.random import randint as np_randint


print("\nrandom.randint")
distribution_timer(randint, 1, 10)

print("\nRandom_Int.random_int")
distribution_timer(random_int, 1, 10)

print("\nnumpy.np_randint")
distribution_timer(np_randint, 1, 10)
