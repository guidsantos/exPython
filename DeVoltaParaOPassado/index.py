def formatMoney(value):
    formatValue = f'R$ {value:.2f}'.replace('.', ',')
    return formatValue


def calcBiggestDiff(acoesList: list, maxDays: int):
    calcDiff = [-1, 1, 2]
    x = 0
    for acao in acoesList:
        for dayRange in range(0, maxDays+1):
            if x + dayRange <= n - 1:
                diff = acoesList[x+dayRange] - acao
                if calcDiff[0] < diff:
                    calcDiff = [diff, x+1, x+dayRange+1]
        x += 1
    return calcDiff


while True:
    n = int(input('Digite quantos dias serão registrados max(1-30): '))
    if 0 < n <= 30:
        break
    else:
        print('Valor invalido')
        continue

acoes = []
x = 1
for i in range(n):
    i = float(input(f'Digite Valor da ação no {x}º dia: '))
    x += 1
    acoes.append(i)


while True:
    k = int(input('Digite o limite de dias para realizar compra e venda: '))
    if n >= k > 0:
        break
    else:
        print('A quantidade de dias precisa estar dentro da quantidade de registros')
        continue

q = float(input('Digite a quantidade de dinheiro: '))

bestBuy = calcBiggestDiff(acoes, k)
qtdAcoesCompradas = int(q//acoes[bestBuy[1]-1])
lucro = (qtdAcoesCompradas*acoes[bestBuy[2]-1]) - \
    (qtdAcoesCompradas*acoes[bestBuy[1]-1])


buyDay = bestBuy[1]
buyPrice = acoes[buyDay-1]
soldDay = bestBuy[2]
soldPrice = acoes[soldDay-1]

print()
print(f'Dia de compra: {buyDay} ')
print(f'Preço de compra: {formatMoney(buyPrice)} ')
print(f'Dia de venda: {soldDay} ')
print(f'Preço de venda: {formatMoney(soldPrice)} ')
print(f'Quantidade de acoes compradas: {qtdAcoesCompradas} ')
print(f'Dia de compra: {formatMoney(round(lucro,2))} ')
print()
