# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from abc import ABC, abstractmethod

# A classe `Funcionario` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Funcionario(ABC):
    salario_min = 1612
    desconto_inss = 7.5
    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome = None):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0
        

    @abstractmethod
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def calcular_salario(self):
        pass

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def analisar_salario(self):
        pass


# A classe `Horista` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 0, qtd_hora = 0 ):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_hora = qtd_hora
        self.salario_bruto = self.valor_hora * self.qtd_hora

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def calcular_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss) / 100
        return f"Salário --> R${self.salario:.2f}"

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def analisar_salario(self):
        pass

