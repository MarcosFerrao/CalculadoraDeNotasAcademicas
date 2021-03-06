# lista de aunos que será usados para calcular as notas
alunos = {
    'jeffersons':
        {
            'nome': 'Jeffersson santos',
            'trabalhos': [90, 95, 80, 100],
            'provas': [90, 80],
            'laboratorio': [90, 85.2]
        },
    'pedros':
        {
            'nome': 'Pedro Silva',
            'trabalhos': [70, 95, 60, 100],
            'provas': [90, 60],
            'laboratorio': [90, 55.2]
        },
    'marias':
        {
            'nome': 'Maria Souza',
            'trabalhos': [72, 82, 23, 39],
            'provas': [89, 95],
            'laboratorio': [80, 80]
        },
    'angelaf':
        {
            'nome': 'Angela Ferreira',
            'trabalhos': [67, 55, 77, 21],
            'provas': [80, 60],
            'laboratorio': [69, 44.56]
        },
    'marcoss':
        {
            'nome': 'Marcos Soares',
            'trabalhos': [95, 89, 90, 86],
            'provas': [65, 56],
            'laboratorio': [50, 40.6]
        },
}


# 1 Função: obter media das notas
def obter_media(notas):
    """
    Funçã para obter a média das notas  informadas dos alunos.
    :param notas: çista com notas de cada tipo de teste(provas, trabalhos, laboratorio)
    :return: média das notas na lista passada
    """
    total_soma = sum(notas)
    total_soma = float(total_soma)
    return total_soma / len(notas)


# 2 Função: média com base nos pesos
def calcular_media_total(aluno):
    """
    Função que calcula a media total por tipo / pesos
    :param aluno: dicionario com dados do aluno
    :return: média final com bases nos pesos
    """
    trabalhos = obter_media(aluno['trabalhos'])
    provas = obter_media(aluno['provas'])
    laboratorio = obter_media(aluno['laboratorio'])
    return (0.25 * trabalhos + 0.55 * provas + 0.20 * laboratorio)


# 3 Funçao:atribuir a letra de acordo com os pesos
def atribuir_letra_nota(nota_final_aluno):
    """
    Função para atribuir a letra de acordo com a nota final
    :param nota_final_aluno: float(nota final do aluno
    :return: letra da nota com base da nota final.
    """
    if nota_final_aluno >= 90:
        return "A"
    elif nota_final_aluno >= 80:
        return "B"
    elif nota_final_aluno >= 70:
        return "C"
    elif nota_final_aluno >= 60:
        return "D"
    else:
        return "F"


# 4 media da classe
def nota_media_classe():
    """
    Funçõ para calcular a média final da turma.
    :return: Média final.
    """
    resultado_lista = []
    for aluno, detalhes in alunos.items():
        media_aluno = calcular_media_total(alunos[aluno])
        resultado_lista.append(media_aluno)
    return obter_media(resultado_lista)
