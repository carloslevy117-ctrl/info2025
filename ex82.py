# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V8.2

file = "frase.txt"

with open(file,"r") as f:
    linhas = f.readlines()
    numLinhas = len(linhas)
    print(numLinhas,"linhas")