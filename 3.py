"""
3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração,
multiplicação e divisão). O usuário deve informar dois números e o programa deve
fazer as quatro operações. (modifique para calcular tudo no mesmo método, somando
1 ao resultado de cada operação)
"""
class Calculadora:
    def soma(self, n1, n2):
        soma=n1+n2+1
        print("A soma (+ 1) é igual a: ",soma)

    def sub(self, n1, n2):
        sub=n1-n2+1
        print("A diferença (+ 1) é igual a: ",sub)

    def div(self, n1, n2):
        div=(n1/n2)+1
        print("A divisão (+ 1) é igual a: ",div)

    def mult(self, n1, n2):
        mult=(n1*n2)+1
        print("A multiplicação (+ 1) é igual a: ",mult)

calculo=Calculadora()
opçao=-1

while opçao!=0:

    opçao=int(input("Digite uma opção para continuar: \n1- SOMA \n2-SUBTRAÇÃO \n3-DIVISÃO \n4-MULTIPLICAÇÃO \n0-SAIR\n"))

    if opçao==0:
        print("Obrigado por utilizar a calculadora!")
        break

    n1=int(input("Digite o primeiro número do cálculo: "))
    n2=int(input("Digite o segundo número do cálculo: "))


    if opçao==1:
        calculo.soma(n1,n2)

    if opçao==2:
        calculo.sub(n1,n2)

    if opçao==3:
        calculo.div(n1,n2)

    if opçao==4:
        calculo.mult(n1,n2)

    if opçao<0 or opçao>4:
        print("Número inválido. Tente novamente.")
        opçao=int(input("Digite uma opção para continuar: \n1- SOMA \n2-SUBTRAÇÃO \n3-DIVISÃO \n4-MULTIPLICAÇÃO \n0-SAIR"))
