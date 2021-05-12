def calcVolume(d, h):
    return ((3.14*(d/2)**2)*h)*1000


def abastecimento(diametro, comprimento, demandPostoA, demandPostoB, demandPostoC):
    volume = calcVolume(diametro, comprimento)

    if volume >= demandPostoA:
        volume -= demandPostoA
        print('posto A foi reabastecido')
    elif volume < demandPostoA:
        print('posto A não foi reabastecido')
    if volume >= demandPostoB:
        volume -= demandPostoB
        print('posto B foi reabastecido')
    elif volume < demandPostoB:
        print('posto B não foi reabastecido')
    if volume >= demandPostoC:
        print('posto C foi reabastecido')
    elif volume < demandPostoC:
        print('posto C não foi reabastecido')


d = float((input('Insira o Diâmetro do Caminhão em metros: ')))
h = float((input('Insira o Comprimento do Caminhão em metros: ')))
postA = float((input('Insira a demanda do Posto A em litros: ')))
postB = float((input('Insira a demanda do Posto B em litros: ')))
postC = float((input('Insira a demanda do Posto C em litros: ')))


abastecimento(d, h, postA, postB, postC)
