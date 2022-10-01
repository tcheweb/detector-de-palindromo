### DETECTOR DE PALÍNDROMOs #####################
### Por Adriano Baumart
### Versão: 1.0.1       Data: 15/09/2022
### Desafio do Curso de Pyhton
#################################################
# Exemplos de palíndromos para teste
# Apos a sopa
# A Sacada da casa
# A torre da derrota
# O lobo ama o bolo
# Anoratam a data da maratona

print(' DETECTOR DE PALÍNDROMO ')
print('=-'*20)

frase = str(input('Digite uma frase: '))
semespaco = frase.replace(' ', '').upper()  #Remove os espaços da frase digitada
invert = semespaco[::-1]

print('O inverso de {} é {}.'.format(semespaco, invert))
if semespaco == invert:
    print('"{}" É UM PALÍNDROMO!'.format(frase))
else:
    print('"{}" NÃO É um palíndromo'.format(frase))







