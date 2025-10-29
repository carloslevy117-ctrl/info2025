# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V7.3


from random import randint

lista = []


for n in range(25):
    while True:
        num_sorteado = randint(1, 40)
        if num_sorteado not in lista:
            lista.append(num_sorteado)
            break

lista_ordenada = sorted(lista)

print(lista_ordenada)

