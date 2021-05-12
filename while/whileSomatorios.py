# Soma dos N primeiros naturais

N = int(input('Insira a quantidade de números a serem somados: '))

k = 1
S = 0

while k <= N:
    S += k
    k += 1

print(f'Resultado da soma = {S}')
