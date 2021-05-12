def exibirHP(hpRyu, hpKen):
    print(f'HP RYU ', end=' ')
    print(f'##'*(hpRyu//10), end=' ')
    print(f'<{hpRyu}>')
    print(f'HP Ken ', end=' ')
    print(f'##'*(hpKen//10), end=' ')
    print(f'<{hpKen}>')


def exibirResultado(nGolpesRyu, nGolpesKen, nomeVencedor: str):
    print(f'LUTADOR VENCEDOR: {nomeVencedor}')
    print(f'GOLPES RYU = {nGolpesRyu}')
    print(f'GOLPES KEN = {nGolpesKen}')


def fight():
    hpRyu = int(input('Digite a vida do Ryu: '))
    hpKen = int(input('Digite a vida do Ken: '))
    nGolpesRyu = 0
    nGolpesKen = 0
    while True:
        golpe = int(input('Valor do golpe: '))
        if golpe > 0:
            print(f'<RYU> APLICOU UM GOLPE: {golpe}')
            hpKen -= golpe
            nGolpesRyu += 1
            if hpKen <= 0:
                hpKen = 0
            exibirHP(hpRyu, hpKen)
        elif golpe < 0:
            print(f'<KEN> APLICOU UM GOLPE: {golpe * -1}')
            hpRyu += golpe
            nGolpesKen += 1
            if hpRyu <= 0:
                hpRyu = 0
            exibirHP(hpRyu, hpKen)
        if hpKen <= 0:
            exibirResultado(nGolpesRyu, nGolpesKen, 'RYU')
            break
        elif hpRyu <= 0:
            exibirResultado(nGolpesRyu, nGolpesKen, 'KEN')
            break


fight()
