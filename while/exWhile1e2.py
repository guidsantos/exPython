# 1 Escreva um programa sabendo que 1lb = 0,454kg, imprime uma tabela contendo valores em libra e o respectivo em kg
# variando de 1 á 100 de 5 em 5 libras iniciando em 1 e sem segudia os valores 5, 10, 15,20 ... 10

print('\n\n')
print('='*30)

k = 1
lb = 0.454
while k <= 100:
    if k == 1:
        print(f'{k}lb equivale á {k*lb:.3f}kg ')
        k += 4
    else:
        print(f'{k}lb equivale á {k*lb:.3f}kg ')
        k += 5


print('\n\n')
print('='*30)

# 2 Escrever um programa que faz a leitura de N números inteiros e imprime apenas o maior número digitado.
# O valor de N também deverá ser lido

qtdNum = int(input("Quantos números deseja inserir: "))

k = 1

while k <= qtdNum:
    if qtdNum > 0:
        x = int(input("Digite um número inteiro: "))
        if k == 1 or x > maiorNum:
            maiorNum = x
    k += 1

print(f'\nO maior número digitado foi {maiorNum}')
