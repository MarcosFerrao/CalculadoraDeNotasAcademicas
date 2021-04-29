"""
Programa para criar uma calculador de notas acadêmcas em Python

Dados diferentes e éso e otas dos alinos, precisamo encontrar as notas finais.
A pontuação da prova é uma média das respectivas notas(provas, trabalhos, laboratório).

A pontuação final da prova é atribuida usando a formíla abaixo.
25% das notas obtidas na submissão de trabalhos.
55% das notas obtidas nas provas
28% das notas obtidas no laboratório

A nota será calculada de acordo com:
1. pontuação >= 90: "A"
2. pontuação >= 80: "B"
3. pontuação >= 70: "C"
4. pontuação >= 60: "D"

Além disso calcule a média total da classe e a nota da classe.
"""

from helpers import alunos, calcular_media_total, atribuir_letra_nota, nota_media_classe

if __name__ == '__main__':
    # for looping para percorrer a lista dos alunos.

    for aluno, detalhe in alunos.items():
        print(f"\n ---- {alunos[aluno]['nome']} ----")
        media_total_aluno = round(calcular_media_total(alunos[aluno]), 2)
        print(f"\t -Média da nota do aluno(a) {alunos[aluno]['nome']} é: {media_total_aluno}")
        print(f"\t -Nota final do aluno(a) {alunos[aluno]['nome']} é : {atribuir_letra_nota(media_total_aluno)}")

    # calcula a média da classe.
    media_classe = nota_media_classe()

    print(f"\nMedia da turma: {round(media_classe, 2)}")
    print(f"Nota final da classe é: {atribuir_letra_nota(media_classe)}")
