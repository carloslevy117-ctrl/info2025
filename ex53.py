# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V5.3


#begin_inputs
 

#end_inputs
anos = 0
taipu = 12000
ceara_mirim = 73000
parnamirim = 250000
popu_ceara_mirim = 0.03
popu_taipu = 0.01
popu_parnamirim = 0.10
while parnamirim > ceara_mirim or parnamirim > taipu:
    ceara_mirim = ceara_mirim + (ceara_mirim + popu_ceara_mirim)
    taipu = taipu + (taipu + popu_taipu)
    parnamirim = (parnamirim + popu_parnamirim)
    anos += 1
print(anos)