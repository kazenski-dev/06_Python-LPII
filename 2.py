"""
2 - Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo,
e mostre-o por extenso. Este número deverá variar entre 1 e 5. Se o usuário introduzir
um número que não pertença a este intervalo, mostre a frase “número inválido”.
"""

numero=int(input("Digite um número: "))

if numero==1:
    print("Um.")
if numero==2:
    print("Dois.")
if numero==3:
    print("Três.")
if numero==4:
    print("Quatro.")
if numero==5:
    print("Cinco.")

if numero<1 or numero>5:
    print("Número inválido.")
