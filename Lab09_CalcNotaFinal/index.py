def inserirItensLista(lista: list, qtdItens: int, input_text: str, input_type=float):
    for i in range(1, qtdItens+1):
        valor = input_type(input(f'{input_text} {i}º nota: '))
        lista.append(valor)


def aprovadoOuReprovado(nota: float, media: float = 5.0):
    if nota >= media:
        return 'Aprovado'
    elif nota < media:
        return 'Reprovado'


def calcMediaPonderada(lista_notas: list, lista_pesos: list):
    notas_ponderadas = []
    for i in range(len(lista_notas)):
        notas_ponderadas.append(lista_notas[i] * lista_pesos[i])

    soma_notas = sum(notas_ponderadas)
    produto_pesos = sum(lista_pesos)

    return soma_notas/produto_pesos


def formatarNota(nota: float):
    return f'{nota:.1f}'.replace('.', ',')


# Receber quantidade de notas
n = int((input("Quantas notas deseja inserir: ")))

notas = []
pesos = []

# Inserir notas e pesoas do lab
inserirItensLista(notas, n, 'Digite a')
inserirItensLista(pesos, n, 'Digite o peso da', int)

# Calcular media do lab
media_lab = calcMediaPonderada(notas, pesos)


def mostrarResultado(media_lab: float, situacao_texto: str, nota_final: float = ''):
    if nota_final == '':
        nota_final = media_lab
    situacao = aprovadoOuReprovado(nota_final)

    print(f'\nMedia Laboratorios: {formatarNota(media_lab)}')
    print(f'Situacao: {situacao} {situacao_texto}')
    print(f'Nota Final: {formatarNota(nota_final)}\n')


# Verificar se será reprovado ou aprovado por nota
if media_lab >= 5:
    mostrarResultado(media_lab, 'por nota')
elif media_lab < 2.5:
    mostrarResultado(media_lab, 'por nota')
# Verificar se tera notas de exame
elif media_lab:
    # Receber quantidade de notas do exame:
    m = int(input('Quantidade de notas no exame: '))

    notas_exame = []
    pesos_exame = []

    # Inserir notas e pesos dos exames
    inserirItensLista(pesos_exame, m, 'Digite o peso da', int)
    inserirItensLista(notas_exame, m, 'Digite a')

    # Calcular media exame
    media_exame = calcMediaPonderada(notas_exame, pesos_exame)

    # Calculoca nota final
    nota_final = min(5, (media_lab + media_exame) / 2)
    mostrarResultado(media_lab, 'no exame', nota_final)
