import os


def candidatos():
    print('='*20)
    print('Resultado da eleição: ')
    print(f'Codigo  | Candidatos')
    print(f'11      | João')
    print(f'45      | Maria')
    print(f'0       | Voto em branco')
    print('='*20)


def resultado(candidato11, candidato45, votosNulos, NumEleitores):
    qtdVotos = (candidato11 + candidato45 + votosNulos)
    porcentagemVotos = (qtdVotos/NumEleitores)*100

    print('='*20)
    print('SESSÃO ENCERRADA')
    print('='*20)
    print(f'Total de eleitores: {NumEleitores}')
    print(f'Quantidade Votos: {qtdVotos}')
    print(f'Porcentagem de Votos: {porcentagemVotos:.1f}%')
    print('='*20)
    print(f'Votos  | Candidatos')
    print(f'{candidato11}      | João')
    print(f'{candidato45}      | Maria')
    print(f'{votosNulos}      | Voto em branco')
    print('='*20)


def urna(NumEleitores):
    candidato11 = 0
    candidato45 = 0
    votosNulos = 0
    N = 1

    while N <= NumEleitores:
        candidatos()
        voto = int(input('\nInsira seu voto: '))
        if voto == 1234:
            tentativas = 0
            while tentativas < 3:
                senha = int(input('Insira a senha: '))
                if senha != 3571:
                    tentativas += 1
                elif senha == 3571:
                    N = NumEleitores + 1
                    break
        elif voto == 11:
            candidato11 += 1
        elif voto == 45:
            candidato45 += 1
        elif votosNulos == 0:
            votosNulos += 1
        else:
            votosNulos += 1
        os.system('cls')
        N += 1

    resultado(candidato11, candidato45, votosNulos, NumEleitores)


NumEleitores = int(input('Quantas pessoas iram votar: '))

urna(NumEleitores)
