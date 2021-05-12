# Calcule a media e se foi aprovado
# Atividades: a1, a2,a3 - se não foi feito a3=0
# Média prática MP

# Calcular
# MT (0,4*A1 + 0,6*A2) ou (0,4*A1 + 0,6*A3) ou (0,4*A3 + 0,6*A2) => escolher melhor opção
# MF se MT e MP>= 5 então MF = 0,5*MT + 0,5*MP
# senão MF = min(MT,MP)
# Imprimir Aprovado ou reprovado se MF>=5

def calcMedia(a1, a2, a3, mp):

    p1 = (0.4*a1 + 0.6*a2)
    p2 = (0.4*a1 + 0.6*a3)
    p3 = (0.4*a3 + 0.6*a2)

    mt = max(p1, p2, p3)

    if mt and mp >= 5:
        mf = 0.5*mt + 0.5*mp
    else:
        mf = min(mt, mp)

    if mf >= 5:
        print(f'Aprovado com {mf:.1f}')
    else:
        print(f'Reprovado com {mf:.1f}')


a1 = float(input("Digite a nota da Atividade1: "))
a2 = float(input("Digite a nota da Atividade2: "))
a3 = float(input("Digite a nota da Atividade3: "))
mp = float(input("Digite a nota da MP: "))

calcMedia(a1, a2, a3, mp)
