# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from rich import inspect, print

# A classe `Pessoa` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Pessoa:
    def __init__(self, nome= '', idade= 0):
        self.nome = nome
        self.idade = idade

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fazer_aniversario(self):
        self.idade += 1


# A classe `Aluno` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fazer_matricula(self):
        print(f'{self.nome} matriculado com sucesso.')
    

# A classe `Professor` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def dar_aula(self):
        print(f'Professor {self.nome} dando aula de {self.especialidade} ! ')


# A classe `Funcionario` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo 
        self.setor = setor 

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def bater_ponto(self):
        print(f'Funcionário {self.nome} bateu o ponto. ')


a1 = Aluno('Gui', 32, 'ADS', 'Turma-A')
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor('Gregory', 44, 'Fisica', 'Mestre')
p1.dar_aula()


f1 = Funcionario('Thais', 28, 'CEO', 'Estetica-Calleza')
f1.bater_ponto()

