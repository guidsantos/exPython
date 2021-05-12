# 3) [Deitel, Deitel]Escreva um programa que leia o valor do lado de um quadrado e então imprima o quadrado com asteriscos.
# Seu programa deve funcionar com quadrados de todos os tamanhos entre 1 e 29

num = int(input('Insira o tamanho do quadrado de 1 a 29: '))

if 1 <= num <= 29:
    print(f'Quadrado de tamanho {num} \n')
    n = num
    while n > 0:
        print('*'*num)
        n -= 1
