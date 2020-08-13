"""
3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração,
multiplicação e divisão). O usuário deve informar dois números e o programa deve
fazer as quatro operações.
"""
class Calculadora:
    def soma(self, n1, n2):
        soma=n1+n2
        print("A soma é igual a: ",soma)

    def sub(self, n1, n2):
        sub=n1-n2
        print("A diferença é igual a: ",sub)

    def div(self, n1, n2):
        div=n1/n2
        print("A divisão é igual a: ",div)

    def mult(self, n1, n2):
        mult=n1*n2
        print("A multiplicação é igual a: ",mult)

calculo=Calculadora()

n1=int(input("Digite o número 1: "))
n2=int(input("Digite o número 2: "))

calculo.soma(n1,n2)
calculo.sub(n1,n2)
calculo.div(n1,n2)
calculo.mult(n1,n2)
