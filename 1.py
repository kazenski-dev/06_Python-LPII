"""
Escreva uma classe que contém um método que calcule se a pessoa é maior de 18
anos ou não. Receba os dados pela console e chame este método. (modifique este
exercício para receber 5 alunos, 3 notas para cada um e calcule a média mostrando se
está aprovado ou não)
"""

class Validar_dezoito:
    def maior_idade(self,nome, idade):
        if idade>=18:
            print(nome,"é maior de 18 anos.")
        else:
            print(nome,"é menor de 18 anos.")

#--------------------------------------------------------------------

class MediaAlunos:
    def media_final(self,nota1, nota2, nota3):
        media_aluno=(nota1 + nota2 + nota3)/3
        if media_aluno>=7:
            print("Média: ", media_aluno, " | " , "Aprovado!")
        else:
            print("Média: ", media_aluno, " | ", "Reprovado :(")


qt_alunos=4
while qt_alunos!=-1:

    nome_aluno=input("Digite o nome do aluno: ")
    idade=int (input("Digite a idade do aluno: "))
    nota1=float(input("Digite a primeira nota do aluno: "))
    nota2=float(input("Digite a segunda nota do aluno: "))
    nota3=float(input("Digite a terceira nota do aluno: "))
    qt_alunos-=1

    dezoito = Validar_dezoito()
    dezoito.maior_idade(nome_aluno,idade)

    Media_Alunos=MediaAlunos()
    Media_Alunos.media_final(nota1,nota2,nota3)
