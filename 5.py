"""
5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como
positivo).
"""

class determinar:
    def positivo_negativo(self,num):
        if num>=0:
            print("O número", num,"é positivo.")

        else:
            print("O número", num, "é negativo.")

determinar=determinar()
num=int(input("Digite um número: "))
determinar.positivo_negativo(num)
