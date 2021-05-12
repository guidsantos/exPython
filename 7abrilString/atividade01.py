frase = str(input('Digite uma frase de até 500 caracteres: '))


if len(frase) <= 500:
    palavra = str(input('Digite uma palavra a ser encontrada na frase: '))

    qtdPalavras = frase.count(palavra)

    if qtdPalavras > 0:
        strQtdPalavras = str(f'apareceu {qtdPalavras} vezes na frase')
    else:
        strQtdPalavras = 'Não foi encontrada na frase'

    print(f'\nNa frase: ( {frase} )\nA palavra ({palavra}), {strQtdPalavras}')
else:
    print(f'\nA frase possui mais de 500 caracteres')
