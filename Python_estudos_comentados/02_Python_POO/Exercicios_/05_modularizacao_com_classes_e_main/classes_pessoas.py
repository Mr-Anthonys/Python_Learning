# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# A classe `Pessoa` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Pessoa:
    """
    Classe ancestral, tem nome e idade da pessoa e um metodo de fazer aniversario.
    """
    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome= '', idade= 0):
        self.nome = nome
        self.idade = idade

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fazer_aniversario(self):
        self.idade += 1


# A classe `Aluno` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Aluno(Pessoa):
    """
    Classe Aluno, derivada da ancestral (é uma Pessoa) então vai herdar nome e idade e fazer aniversario
    Atributos e Metodos proprios: curso e turma, e fazer matricula()"""

    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fazer_matricula(self):
        print(f'{self.nome} matriculado com sucesso.')
    

# A classe `Professor` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Professor(Pessoa):
    """
    Classe professor, derivada da ancestral (Pessoa), é uma Pessoa
    Atributos e Metodos: especialidade, nivel e dar aula()."""

    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def dar_aula(self):
        print(f'Professor {self.nome} dando aula de {self.especialidade} ! ')


# A classe `Funcionario` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Funcionario(Pessoa):
    """Classe Funcionário é uma Pessoa(), e possui cargo, setor
    Metodo adicional: Baterponto()"""
    
    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo 
        self.setor = setor 

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def bater_ponto(self):
        print(f'Funcionário {self.nome} bateu o ponto. ')

