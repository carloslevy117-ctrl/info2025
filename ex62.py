# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V6.2


#begin_inputs
n = int(input(""))

#end_inputs

def trianguloretangulo(n):
    for i in range(1, n + 1):
        for r in range(1, i + 1):
            print(r, end=' ')
        print()
trianguloretangulo(n)