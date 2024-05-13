import textwrap
from datetime import datetime # Biblioteca de manipulação de data e hora

# Sistema de matrícula de alunos

# Lista todas as salas e seus respectivos alunos
class Sala:
    def __init__(self):
        self.escola = []

    def adicionar_aluno(self, aluno, serie):
        self.escola.append((aluno, serie))

    def listar_salas(self):
        for alunos, salas in self.escola:
            print(alunos, salas)

# Pega os dados do aluno
class Aluno:
    def __init__(self, rg, cpf, nome, data_nascimento):
        self._rg = rg
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()
        self._ano_atual = datetime.now().date().year

    # Método __str__ retorna uma string formatada dos valores contidos no construtor
    def __str__(self):
            return f"{self.__class__.__name__}: {self._nome}, Idade: {self._ano_atual - self._data_nascimento.year} anos"

# Pega ano e a turma do aluno
class Serie:
    def __init__(self, ano, turma):
        self._ano = ano
        self._turma = turma

    # Método __str__ retorna uma string formatada dos valores contidos no construtor
    def __str__(self):
        return f"Escola: MATRIX - {self._ano}ª{self._turma}"


def mensagem():
    texto = """
    -----------------------------------
    E. E. E. FUNDAMENTAL E MÉDIO MATRIX
    -----------------------------------
     - SISTEMA DE CADASTRO DE ALUNOS -
    -----------------------------------
    """
    return textwrap.dedent(texto)

def main():
    salas = Sala()

    while True:
        print(mensagem())

        # O responsável irá preencher os dados do aluno
        nome = input('Nome: ')
        rg = input('RG: ')
        cpf = input('CPF: ')
        data_nascimento = input('Data de nascimento - (12-12-2012): ')
        ano = int(input('Série: '))
        turma = input('Turma: ')

        # Objeto aluno e sal, realizam atribuição dos valores às instâncias da classe
        aluno = Aluno(rg, cpf, nome, data_nascimento)
        sala = Serie(ano, turma)

        # Classe salas irá adicionar os alunos em uma lista
        salas.adicionar_aluno(aluno, sala)

        print("Aluno adicionado à sala!")

        print('\n----------------------------------')
        continuar = input('Quer continuar? [s/n] ')
    
        if continuar == 'n':
            # Mostra a lista de alunos
            print("\nLista de Alunos:")
            salas.listar_salas()
            break

main()
