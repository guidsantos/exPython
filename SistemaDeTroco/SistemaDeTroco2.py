def troco(pagamento, compra):
    print("Pagamento: ", pagamento)
    print("Valor da Compra: ", compra)

    notas = [100, 50, 20, 10, 5, 1]

    troco = pagamento - compra
    if troco >= 0:
        print('Troco: R$ %.2f\n' % troco)
        print('Precisará devolver:\n')
        for nota in notas:
            if troco >= nota:
                quantNotas = troco//nota
                restoTroco = troco - nota*quantNotas
                print('%i notas de R$%.2f' % (quantNotas, nota))
                troco = restoTroco
        print("\nFim")
    else:
        print('O Dinheiro pago é insuficiente para compra')


pag = float(input("Valor Pago: "))
comp = float(input("Valor da Compra: "))

troco(pag, comp)
