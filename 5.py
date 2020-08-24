"""
5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como
positivo). (modifique para saber se é par ou ímpar)
"""

class determinar:
    def positivo_negativo(self,num):
        if num>0 and num%2==0:
            print("O número", num,"é positivo e par.")

        if num<0 and num%2==0:
            print("O número", num, "é negativo e par.")

        if num<0 and num%2!=0:
            print("O número", num, "é negativo e ímpar.")

        if num>0 and num%2!=0:
            print("O número", num, "é positivo e ímpar.")

determinar=determinar()
num=int(input("Digite um número: "))
determinar.positivo_negativo(num)
