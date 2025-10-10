# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V5.2


#begin_inputs
 

#end_inputs

minutos=0
distancia_tartaruga=500
vel_tartaruga=1
vel_lebre=10
while True:
    distancia_tartaruga+=vel_tartaruga
    distancia_lebre=vel_lebre*minutos
    if distancia_lebre>=distancia_tartaruga:
        break
    minutos+=1
print(minutos)