def chegadaEstacao(x, t, v1, v2):
    s1 = (x/v1)
    s2 = (x/v2) + t/60
    if s1 < s2:
        print('True')
    elif s1 == s2:
        print('Chegaram Juntos')
    else:
        print('False')


print('Descobrir se o 1º Trem chegou antes do 2º Trem \n')
x = int(input('Distancia em km entre as duas estacoes: '))
t = int(input('Diferenca em minutos do tempo de saida dos dois trens: '))
v1 = float(input('Velocidade do Trem1 (km/h): '))
v2 = float(input('Velocidade do Trem2 (km/h): '))

chegadaEstacao(x, t, v1, v2)
