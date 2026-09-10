# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

# ABD --> Abstract Base Classes
from abc import ABC, abstractmethod # abstractmethod (Criar métodos abstratos na clase ancestral, pai, mãe)


# A classe `Pessoa` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Pessoa(ABC): #  
  
    def __init__(self, nome= '', idade= 0):
        self.nome = nome
        self.idade = idade

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod # Criado um método abstrado na classe ancestral

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def estudar(self):
        pass


# A classe `Aluno` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Aluno(Pessoa):


    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fazer_matricula(self):
        print(f'{self.nome} matriculado com sucesso.')

    # Declarando o metodo da ancestral na derivada
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def estudar(self):
        print(f'Aluno {self.nome} está estudando para o seu curso {self.curso}')   

# A classe `Professor` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Professor(Pessoa):
    
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def dar_aula(self):
        print(f'Professor {self.nome} dando aula de {self.especialidade} ! ')

    # Declarando o metodo da ancestral na derivada
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def estudar(self):
        print(f'Professor {self.nivel} em {self.especialidade} está estudando ') 


# A classe `Funcionario` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Funcionario(Pessoa):
    
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo 
        self.setor = setor 

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def bater_ponto(self):
        print(f'Funcionário {self.nome} bateu o ponto. ')

     # Declarando o metodo da ancestral na derivada
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def estudar(self):
        print(f'{self.nome} está estudando para area {self.setor}')
