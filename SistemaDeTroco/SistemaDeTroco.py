def troco(pagamento, compra):
    print("Pagamento: ", pagamento)
    print("Valor da Compra: ", compra)

    notas = [100, 50, 20, 10, 5, 1]

    troco = pagamento - compra
    if troco >= 0:
        print(f'\nTroco: R$ {troco:.2f}\n')
        print('Precisa devolver:\n')
        for nota in notas:
            if troco >= nota:
                quantNotas = int(troco//nota)
                restoTroco = troco - nota*quantNotas
                print(f'{quantNotas} nota(s) de R${nota:.2f}')
                troco = restoTroco
        print("\nFim")
    else:
        print('O Dinheiro pago é insuficiente para compra')


pag = float(input("Valor Pago: "))
comp = float(input("Valor da Compra: "))

troco(pag, comp)
