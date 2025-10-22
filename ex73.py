# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V7.3


import random

def sorteio_loteria():
    numeros = random.sample(range(1, 41), 25)
    numeros.sort()
    return numeros
print(sorteio_loteria())


