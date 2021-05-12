def separarLinhas(frase):
    linhas = []
    palavras = frase.split()
    linha = []
    tamanhoLinha = 0
    for palavra in palavras:
        tamanhoLinha += len(palavra) + 1
        if tamanhoLinha < 51:
            linha.append(palavra)
        elif tamanhoLinha == 51:
            linha.append(palavra)
            linhas.append(linha)
            tamanhoLinha = 0
            linha = []
        elif tamanhoLinha > 51:
            linhas.append(linha)
            linha = []
            tamanhoLinha = 0
            linha.append(palavra)
            tamanhoLinha += len(palavra) + 1
    if linha != []:
        linhas.append(linha)
    for linha in linhas:
        print(' '.join(linha))


frase = str(input('Digite uma frase de até 1000 caracteres: '))

print()

if len(frase) <= 1000:
    separarLinhas(frase)

else:
    print('Frase invalida possui mais de 1000 caracteres')
