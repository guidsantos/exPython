def formatMoney(value):
    formatValue = f'R$ {value:.2f}'.replace('.', ',')
    return formatValue


def descINSS(salarioBruto):
    descontINSS = 0.075
    salarioBrutoValue = salarioBruto
    if 1045.00 < salarioBruto <= 2089.60:
        descontINSS = 0.09
    if 2089.61 < salarioBruto <= 3134.40:
        descontINSS = 0.12
    if 3134.41 < salarioBruto <= 6101.06:
        descontINSS = 0.14
    if salarioBruto > 6101.06:
        descontINSS = 0.14
        salarioBrutoValue = 6101.06

    descINSS = salarioBrutoValue * descontINSS
    print(f'INSS: {formatMoney(descINSS)}')

    salarioLiq = salarioBruto - descINSS

    return salarioLiq


def descIR(salarioINSS):
    descontIR = 0
    parcelaIR = 0
    if 1903.99 < salarioINSS <= 2826.65:
        descontIR = 0.075
        parcelaIR = 142.8
    if 2826.66 < salarioINSS <= 3751.05:
        descontIR = 0.15
        parcelaIR = 354.8
    if 3751.06 < salarioINSS <= 4664.68:
        descontIR = 0.225
        parcelaIR = 636.13
    if salarioINSS >= 4664.67:
        descontIR = 0.275
        parcelaIR = 869.36

    descIR = (salarioINSS * descontIR) - parcelaIR
    print(f'IR: {formatMoney(descIR)}')

    salarioLiq = salarioINSS - descIR

    return salarioLiq


def calcSalario(salarioBruto):

    print(f'Bruto: {formatMoney(salarioBruto)}')

    salarioINSS = descINSS(salarioBruto)
    salarioLiq = descIR(salarioINSS)

    print(f'Liquido: {formatMoney(salarioLiq)}')


salarioBruto = float(input('Digite o salario bruto: '))

calcSalario(salarioBruto)
