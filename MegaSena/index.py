def allAlternateParityInRange(n1: int, n3: int):
    n2 = []
    if n1 % 2 == 0:
        for n in range(n1, n3):
            if n % 2 != 0 & n != n1 | n3:
                n2.append(n)
    elif n1 % 2 != 0:
        for n in range(n1, n3):
            if n % 2 == 0 & n != n1 | n3:
                n2.append(n)

    return [n1, n2, n3]


def multiple7Or13(n123: list, n456: list):
    n1 = n123[0]
    n3 = n123[2]
    n4 = n456[0]
    n6 = n456[2]
    alternatives = []
    for n2 in n123[1]:
        for n5 in n456[1]:
            sumN = n1 + n2 + n3 + n4 + n5 + n6
            div7 = sumN % 7 == 0
            div13 = sumN % 13 == 0
            if div7 | div13 != True:
                alternative = [n1, n2, n3, n4, n5, n6]
                alternatives.append(alternative)
    return alternatives


def nPar(nAfter: int, Nth: int, nAfterTh: int):
    n = 1
    while n % 2 != 0:
        n = int(input(f'Digite o {Nth}º numero: '))
        if n < nAfter:
            n = 1
            print(f'\nO {Nth}º Numero precisa ser maior que o {nAfterTh}º')
        elif n == nAfter:
            n = 1
            print(f'\nO {Nth}º Numero precisa ser diferente do {nAfterTh}º')
        elif n % 2 != 0:
            print(f'\nO {Nth}º Numero precisa ser par')
    return n


def nImpar(nAfter: int, Nth: int, nAfterTh: int):
    n = 2
    while n % 2 == 0:
        n = int(input(f'Digite o {Nth}º numero: '))
        if n < nAfter:
            n = 2
            print(f'\nO {Nth}º Numero precisa ser maior que o {nAfterTh}º')
        elif n == nAfter:
            n = 2
            print(f'\nO {Nth}º Numero precisa ser diferente do {nAfterTh}º')
        elif n % 2 == 0:
            print(f'\nO {Nth}º Numero precisa ser impar')
    return n


n1 = int(input('Digite o 1º numero: '))
if n1 % 2 == 0:
    n3 = nPar(n1, 3, 1)
    n4 = nImpar(n3, 4, 3)
    n6 = nImpar(n4, 6, 4)
elif n1 % 2 != 0:
    n3 = nImpar(n1, 3, 1)
    n4 = nPar(n3, 4, 3)
    n6 = nPar(n4, 6, 4)

n123 = allAlternateParityInRange(n1, n3)
n456 = allAlternateParityInRange(n4, n6)
alternatives = multiple7Or13(n123, n456)

print(f'\nLista de possiveis apostas:\n')
for alt in alternatives:
    print(
        f'{alt[0]:02} - {alt[1]:02} - {alt[2]:02} - {alt[3]:02} - {alt[4]:02} - {alt[5]:02}')
print()
