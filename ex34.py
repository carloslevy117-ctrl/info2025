# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V3.4


#begin_inputs
# programa sem entrada (input)
#end_inputs
dia = 1
mes = 1
ano = 2017
while ano <= 2020:
    mes = 1
    while mes <= 12:
        dia = 1
        while dia <=  30:
            print(f'{dia}/{mes}/{ano}')
            dia += 1
        mes += 1
    ano += 1

	
