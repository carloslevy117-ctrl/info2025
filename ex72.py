# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V7.2


#begin_inputs
letras = ['l', 'r', 'e', 't',"f", 'v',"r","y"]
palavra = 'levy'
#end_inputs

def advinhou_palavra(letras, palavra):
    for letra in palavra:
        if letra not in letras:
            return False
    return True
print(advinhou_palavra(letras, palavra))