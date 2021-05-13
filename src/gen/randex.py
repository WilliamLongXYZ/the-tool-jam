import random


def randfloat(minimum, maximum):
    return minimum + (maximum-minimum)*random.random()

def randbool():
    return bool(random.getrandbits(1))