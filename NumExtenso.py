def numExtenso(n):
    numerosExtensos = {
        1: 'um',
        2: 'dois',
        3: 'tres',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove'
    }

    return print(numerosExtensos.get(n, 'Este Número não foi encontrado'))


x = int(input('Insira um número de 1 a 9: '))

numExtenso(x)
