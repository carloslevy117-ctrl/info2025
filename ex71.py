# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V7.1


#begin_inputs
letras = ["a","r","t","h","u","r"]
#end_inputs


from string import ascii_lowercase

def letras_disponiveis(letras):
    return [l for l in ascii_lowercase if l not in letras]

print(letras_disponiveis(letras))