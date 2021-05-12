# 4) Construir um programa que faz a leitura de N números inteiros e contabiliza:
# quantos são pares, quantos são ímpares, quantos são positivos, quantos são negativos e quantos zeros foram digitados.
# Para a construção do algoritmo, deverá ser feita a leitura de um número por vez, testar o que ele é,
# contabilizar e repetir esses passos N vezes. O valor de N deve ser lido também.
# Use o comando while para o processo repetitivo.
# No final imprimir as 4 quantidades contabilizadas. Não usar vetor/lista para a solução do problema.

qtdNum = int(input("Quantos números deseja inserir: "))

k = 1
par = 0
impar = 0
positivos = 0
negativos = 0
zeros = 0

while k <= qtdNum:

    x = int(input("Digite um número inteiro: "))
    if x % 2 == 0:
        par += 1
    else:
        impar += 1
    if x > 0:
        positivos += 1
    if x < 0:
        negativos += 1
    if x == 0:
        zeros += 1
        par -= 1
    k += 1


print(f'\nNumeros Pares: {par} \nNumeros Impares: {impar}')
print(f'Numeros Positivos: {positivos} \nNumeros Negativos: {negativos}')
print(f'Zero(s): {zeros}\n')
