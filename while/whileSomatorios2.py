# Soma dos N primeiros naturais

N = int(input('Insira a quantidade de números a serem somados: '))

k = 2
S = 0

while k <= N*2:
    S += k
    k += 2

print(f'Resultado da soma = {S}')
