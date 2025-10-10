# @cikey 9938fefe4aecf4a9a53709cde00894a5
# @sid 20251174010018
# @aid V5.3


#begin_inputs
 

#end_inputs
CRESC_CEARA_MIRIM = 1.03

CRESC_PARNAMIRIM=1.01

CRESC_TAIPU=1.10

ceara_mirim = 73000

parnamirim = 250000

taipu=12000

ano=2018

while parnamirim >= ceara_mirim or taipu:
    ceara_mirim=round (ceara_mirim*CRESC_CEARA_MIRIM)
    parnamirim = round(parnamirim*CRESC_PARNAMIRIM)
    taipu=round(taipu*CRESC_TAIPU)
ano += 1

print("parnamirim sera cidade em {0}".format(ano))
print("populacao de parnamirim: {0}".format(parnamirim))
print("populacao de ceara-mirim: {0}".format(ceara_mirim))
print("populacao de taipu: {0}".format(taipu))