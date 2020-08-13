"""
Escreva uma classe que contém um método que calcule se a pessoa é maior de 18
anos ou não. Receba os dados pela console e chame este método. (modifique este
exercício para receber 5 alunos, 3 notas para cada um e calcule a média mostrando se
está aprovado ou não)
"""

class Validar_dezoito:
    def maior_idade(self,idade):
        if idade>=18:
            print("Maior de 18 anos.")
        else:
            print("Menor de 18 anos.")
