# https://en.wikipedia.org/wiki/List_of_municipalities_in_the_state_of_S%C3%A3o_Paulo_by_population
# https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Rio_de_Janeiro_por_popula%C3%A7%C3%A3o
# https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_de_Minas_Gerais_por_popula%C3%A7%C3%A3o
import os

listaPopulacao = [['SP', [11_253_503, 'São Paulo'], [1_221_979, 'Guarulhos'], [1_080_113, 'Campinas'],
                   [765_463, 'São Bernardo do Campo']],
                  ['RJ', [6_747_815, 'Rio de Janeiro'], [1_091_737, 'São Gonçalo'],
                   [924_624, 'Duque de Caxias'], [823_302, 'Nova Iguaçu']],
                  ['MG', [2_521_564, 'Belo Horizonte'], [699_097, 'Uberlândia'],
                   [668_949, 'Contagem'], [573_285, 'Juiz de Fora']]]


def calcPopEstado(estado: int, com_estado=True):
    popTotalEstado = 0
    x = 0
    if com_estado == False:
        x = 1
    for cidade in listaPopulacao[estado][1 + x:]:
        popTotalEstado += cidade[0]
    return popTotalEstado, listaPopulacao[estado][0]


def popTotalEstado(lista: list, com_capital=True):
    popTotalEstado = []
    if com_capital == True:
        for estado in range(len(lista)):
            popTotalEstado.append(calcPopEstado(estado))
    elif com_capital == False:
        for estado in range(len(lista)):
            popTotalEstado.append(
                calcPopEstado(estado, com_estado=False))
    return popTotalEstado


def medPopCapitais(lista: list):
    somaPopCapitais = 0
    for estado in lista:
        somaPopCapitais += estado[1][0]
    mediaPopCapitais = (somaPopCapitais/len(listaPopulacao))
    return mediaPopCapitais


def exibirPopEstados(nCidades=5):
    x = 0
    print('Populações Estado Brasileiro')
    print(f'{"Estado":^10}|{"Cidade":^25}|{"População":^16}')
    for estado in listaPopulacao:
        for cidade in range(1, len(estado)):
            print(f' {estado[0]:10}', end='')
            print(f' {estado[cidade][1]:25}', end='')
            populacao = '{0:,}'.format(estado[cidade][0]).replace(',', '.')
            print(f' {populacao:16}', end='')
            print()
            x += 1
            if x % nCidades == 0:
                input(
                    f'Pressione alguma tecla para exibir outras cidades')


print(f'Média População das Capitais: {medPopCapitais(listaPopulacao):.2f}')
print()
print(f'População Total de cada estado:\n {popTotalEstado(listaPopulacao)}')
print()
print(
    f'Popualação Total de cada Estado sem contar Capital: \n{popTotalEstado(listaPopulacao, False)}')
print()
exibirPopEstados(6)
