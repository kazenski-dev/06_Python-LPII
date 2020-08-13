"""
4 - Faça um programa que receba um valor que é o valor pago, um segundo valor que
é o preço do produto e retorne o troco a ser dado.
"""

valor_pago=float(input("Digite o valor a ser pago: "))
valor_produto=float(input('Digite o preço do produto: '))
troco=valor_pago-valor_produto
faltou= valor_produto-valor_pago

if valor_pago==valor_produto:
    print("Não é requerido o troco.")

elif valor_pago>valor_produto:
    print("O troco será de: R$%.2f" % troco )

else:
    print("O valor pago não é suficiente para comprar o produto. Faltaram R$%.2f" % faltou)
